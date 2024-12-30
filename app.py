import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from io import BytesIO

st.set_page_config(page_title="Weekly Contributions Heatmap", layout="wide")

# -- Define members and days
members = [f"Member {i}" for i in range(1, 16)]
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# -- Initialize session state to store weekly contributions
#    DataFrame with members as rows and days as columns
if "contributions" not in st.session_state:
    st.session_state["contributions"] = pd.DataFrame(
        0,
        index=members,
        columns=days
    )

st.title("Weekly Contributions Heatmap")

# -- Sidebar: Select the day
st.sidebar.title("Daily Input")
day_selected = st.sidebar.selectbox("Select the Day", days)

# -- Sidebar: For each member, input 1 or 0
st.sidebar.write(f"Record contributions for {day_selected}:")
temp_values = {}
for member in members:
    # Using a checkbox or radio; here we use checkbox for clarity
    contributed = st.sidebar.checkbox(member, value=False)
    temp_values[member] = 1 if contributed else 0

# -- Sidebar: Button to update the table
if st.sidebar.button("Submit Contributions"):
    for member in members:
        st.session_state["contributions"].loc[member, day_selected] = temp_values[member]
    st.sidebar.success(f"Saved contributions for {day_selected}!")

# -- Main area: Show data
st.subheader("Current Weekly Contributions (1 = contributed, 0 = no contribution)")
st.dataframe(st.session_state["contributions"], use_container_width=True)

# -- Function to generate a heatmap figure
def generate_heatmap(data: pd.DataFrame):
    plt.figure(figsize=(8, 6))
    sns.heatmap(
        data,
        annot=True,       # Show the numeric 0/1 in each cell
        cmap="YlGnBu",
        cbar=True,
        linewidths=0.5
    )
    plt.title("Weekly Contributions Heatmap", fontsize=16)
    plt.tight_layout()
    return plt.gcf()

# -- Main area: Generate the heatmap on demand
if st.button("Generate Heatmap"):
    fig = generate_heatmap(st.session_state["contributions"])

    # Display the plot in the Streamlit app
    st.pyplot(fig)

    # Prepare PNG download
    buf = BytesIO()
    fig.savefig(buf, format="png")
    buf.seek(0)

    # Download button
    st.download_button(
        label="Download Heatmap as PNG",
        data=buf,
        file_name="weekly_contributions_heatmap.png",
        mime="image/png"
    )

# -- Optional: Clear all data
if st.button("Clear All Data"):
    st.session_state["contributions"] = pd.DataFrame(
        0,
        index=members,
        columns=days
    )
    st.success("All contributions have been reset!")
