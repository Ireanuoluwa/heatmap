import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Set page title
st.title("Weekly Activity Heatmap")

# Define names and weekdays
names = ["Alice", "Bob", "Charlie", "Dave", "Eve"]
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

# Create a form to capture the activity (0 or 1) for each person/day
with st.form("admin_form"):
    st.subheader("Enter Activity Status (0 or 1)")
    
    # Prepare a matrix (list of lists) to hold the input
    input_matrix = []
    
    for name in names:
        row_input = []
        st.markdown(f"**{name}'s status**:")
        cols = st.columns(len(days))
        for i, day in enumerate(days):
            # For each day, create a selectbox with options 0 or 1
            value = cols[i].selectbox(
                f"{day}", 
                options=[0, 1], 
                key=f"{name}_{day}"
            )
            row_input.append(value)
        input_matrix.append(row_input)
    
    # Submit button
    submitted = st.form_submit_button("Generate Heatmap")

# Once the form is submitted, construct a DataFrame and display the heatmap
if submitted:
    # Convert the input matrix into a DataFrame
    df = pd.DataFrame(input_matrix, index=names, columns=days)
    
    st.subheader("Activity Data")
    st.dataframe(df)
    
    # Create heatmap using seaborn
    fig, ax = plt.subplots()
    sns.heatmap(df, annot=True, cmap="YlGnBu", cbar=True, ax=ax)
    ax.set_title("Weekly Activity Heatmap", pad=12)
    
    # Render the plot in Streamlit
    st.pyplot(fig)
