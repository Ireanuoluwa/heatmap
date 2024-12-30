import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Set page title
st.title("Weekly Activity Heatmap")

# Define names and weekdays
names = [
    "Gloria", "Baridule", "Shirley", "Dorathy", "Oyinkan",
    "Moshope", "Faith", "Esther", "Suka", "Chioma",
    "Tolani", "Joy", "Ade", "Wura", "Moyin"
]
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
    
    # Create heatmap using seaborn with specified color map for binary data
    fig, ax = plt.subplots()
    # Custom colormap: sky blue for 0, lilac for 1
    cmap = sns.color_palette(["skyblue", "pink"])
    sns.heatmap(df, annot=False, cmap=cmap, cbar=True, ax=ax, cbar_kws={"ticks": [0, 1]})
    ax.set_title("Weekly Activity Heatmap", pad=12)
    
    # Render the plot in Streamlit
    st.pyplot(fig)

# import streamlit as st
# import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt

# # Set page title
# st.title("Weekly Activity Heatmap")

# # Define names and weekdays

# days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

# # Create a form to capture the activity (0 or 1) for each person/day
# with st.form("admin_form"):
#     st.subheader("Enter Activity Status (0 or 1)")
    
#     # Prepare a matrix (list of lists) to hold the input
#     input_matrix = []
    
#     for name in names:
#         row_input = []
#         st.markdown(f"**{name}'s status**:")
#         cols = st.columns(len(days))
#         for i, day in enumerate(days):
#             # For each day, create a selectbox with options 0 or 1
#             value = cols[i].selectbox(
#                 f"{day}", 
#                 options=[0, 1], 
#                 key=f"{name}_{day}"
#             )
#             row_input.append(value)
#         input_matrix.append(row_input)
    
#     # Submit button
#     submitted = st.form_submit_button("Generate Heatmap")

# # Once the form is submitted, construct a DataFrame and display the heatmap
# if submitted:
#     # Convert the input matrix into a DataFrame
#     df = pd.DataFrame(input_matrix, index=names, columns=days)
    
#     st.subheader("Activity Data")
#     st.dataframe(df)
    
#     # Create heatmap using seaborn with specified color map for binary data
#     fig, ax = plt.subplots()
#     # Custom colormap: blue for 0, orange for 1
#     cmap = sns.color_palette(["blue", "orange"])
#     sns.heatmap(df, annot=False, cmap=cmap, cbar=True, ax=ax, cbar_kws={"ticks": [0, 1]})
#     ax.set_title("Weekly Activity Heatmap", pad=12)
    
#     # Render the plot in Streamlit
#     st.pyplot(fig)

# import streamlit as st
# import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt

# # Set page title
# st.title("Weekly Activity Heatmap")

# # Define names and weekdays
# names = [
#     "Alice", "Bob", "Charlie", "Dave", "Eve",
#     "Fiona", "George", "Hannah", "Ian", "Jenna",
#     "Karl", "Linda", "Mike", "Nina", "Oscar"
# ]
# days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

# # Create a form to capture the activity (0 or 1) for each person/day
# with st.form("admin_form"):
#     st.subheader("Enter Activity Status (0 or 1)")
    
#     # Prepare a matrix (list of lists) to hold the input
#     input_matrix = []
    
#     for name in names:
#         row_input = []
#         st.markdown(f"**{name}'s status**:")
#         cols = st.columns(len(days))
#         for i, day in enumerate(days):
#             # For each day, create a selectbox with options 0 or 1
#             value = cols[i].selectbox(
#                 f"{day}", 
#                 options=[0, 1], 
#                 key=f"{name}_{day}"
#             )
#             row_input.append(value)
#         input_matrix.append(row_input)
    
#     # Submit button
#     submitted = st.form_submit_button("Generate Heatmap")

# # Once the form is submitted, construct a DataFrame and display the heatmap
# if submitted:
#     # Convert the input matrix into a DataFrame
#     df = pd.DataFrame(input_matrix, index=names, columns=days)
    
#     st.subheader("Activity Data")
#     st.dataframe(df)
    
#     # Create heatmap using seaborn with specified color map for binary data
#     fig, ax = plt.subplots()
#     # Custom colormap: blue for 0, orange for 1
#     cmap = sns.color_palette(["blue", "orange"])
#     sns.heatmap(df, annot=True, cmap=cmap, cbar=True, ax=ax, fmt="d", cbar_kws={"ticks": [0, 1]})
#     ax.set_title("Weekly Activity Heatmap", pad=12)
    
#     # Render the plot in Streamlit
#     st.pyplot(fig)

# import streamlit as st
# import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt
# from matplotlib.colors import LinearSegmentedColormap

# # Set page title
# st.title("Weekly Activity Heatmap")

# # Define names and weekdays
# names = [
#     "Alice", "Bob", "Charlie", "Dave", "Eve",
#     "Fiona", "George", "Hannah", "Ian", "Jenna",
#     "Karl", "Linda", "Mike", "Nina", "Oscar"
# ]
# days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

# # Create a form to capture the activity (0 or 1) for each person/day
# with st.form("admin_form"):
#     st.subheader("Enter Activity Status (0 or 1)")
    
#     # Prepare a matrix (list of lists) to hold the input
#     input_matrix = []
    
#     for name in names:
#         row_input = []
#         st.markdown(f"**{name}'s status**:")
#         cols = st.columns(len(days))
#         for i, day in enumerate(days):
#             # For each day, create a selectbox with options 0 or 1
#             value = cols[i].selectbox(
#                 f"{day}", 
#                 options=[0, 1], 
#                 key=f"{name}_{day}"
#             )
#             row_input.append(value)
#         input_matrix.append(row_input)
    
#     # Submit button
#     submitted = st.form_submit_button("Generate Heatmap")

# # Once the form is submitted, construct a DataFrame and display the heatmap
# if submitted:
#     # Convert the input matrix into a DataFrame
#     df = pd.DataFrame(input_matrix, index=names, columns=days)
    
#     st.subheader("Activity Data")
#     st.dataframe(df)
    
#     # Create a custom colormap from red to green
#     cmap = LinearSegmentedColormap.from_list("red_green", ["red", "green"], N=256)
    
#     # Create heatmap using seaborn with gradient and embossed effect
#     fig, ax = plt.subplots()
#     sns.heatmap(df, annot=True, cmap=cmap, cbar=True, ax=ax, fmt="d", linewidths=1, linecolor='black')
#     ax.set_title("Weekly Activity Heatmap", pad=12)
    
#     # Adding the effect of cell borders for a pseudo-3D look
#     for _, spine in ax.spines.items():
#         spine.set_visible(True)
#         spine.set_linewidth(0.5)
    
#     # Render the plot in Streamlit
    st.pyplot(fig)

# import streamlit as st
# import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt

# # Set page title
# st.title("Weekly Activity Heatmap")

# # Define names and weekdays
# names = [
#     "Alice", "Bob", "Charlie", "Dave", "Eve",
#     "Fiona", "George", "Hannah", "Ian", "Jenna",
#     "Karl", "Linda", "Mike", "Nina", "Oscar"
# ]
# days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

# # Create a form to capture the activity (0 or 1) for each person/day
# with st.form("admin_form"):
#     st.subheader("Enter Activity Status (0 or 1)")
    
#     # Prepare a matrix (list of lists) to hold the input
#     input_matrix = []
    
#     for name in names:
#         row_input = []
#         st.markdown(f"**{name}'s status**:")
#         cols = st.columns(len(days))
#         for i, day in enumerate(days):
#             # For each day, create a selectbox with options 0 or 1
#             value = cols[i].selectbox(
#                 f"{day}", 
#                 options=[0, 1], 
#                 key=f"{name}_{day}"
#             )
#             row_input.append(value)
#         input_matrix.append(row_input)
    
#     # Submit button
#     submitted = st.form_submit_button("Generate Heatmap")

# # Once the form is submitted, construct a DataFrame and display the heatmap
# if submitted:
#     # Convert the input matrix into a DataFrame
#     df = pd.DataFrame(input_matrix, index=names, columns=days)
    
#     st.subheader("Activity Data")
#     st.dataframe(df)
    
#     # Create heatmap using seaborn with specified color map for binary data
#     fig, ax = plt.subplots()
#     # Custom colormap: red for 0, green for 1
#     cmap = sns.color_palette(["red", "green"])
#     sns.heatmap(df, annot=True, cmap=cmap, cbar=True, ax=ax, fmt="d", cbar_kws={"ticks": [0, 1]})
#     ax.set_title("Weekly Activity Heatmap", pad=12)
    
#     # Render the plot in Streamlit
#     st.pyplot(fig)


# import streamlit as st
# import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt

# # Set page title
# st.title("Weekly Activity Heatmap")

# # Define names and weekdays
# names = [
#     "Alice", "Bob", "Charlie", "Dave", "Eve",
#     "Fiona", "George", "Hannah", "Ian", "Jenna",
#     "Karl", "Linda", "Mike", "Nina", "Oscar"
# ]
# days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

# # Create a form to capture the activity (0 or 1) for each person/day
# with st.form("admin_form"):
#     st.subheader("Enter Activity Status (0 or 1)")
    
#     # Prepare a matrix (list of lists) to hold the input
#     input_matrix = []
    
#     for name in names:
#         row_input = []
#         st.markdown(f"**{name}'s status**:")
#         cols = st.columns(len(days))
#         for i, day in enumerate(days):
#             # For each day, create a selectbox with options 0 or 1
#             value = cols[i].selectbox(
#                 f"{day}", 
#                 options=[0, 1], 
#                 key=f"{name}_{day}"
#             )
#             row_input.append(value)
#         input_matrix.append(row_input)
    
#     # Submit button
#     submitted = st.form_submit_button("Generate Heatmap")

# # Once the form is submitted, construct a DataFrame and display the heatmap
# if submitted:
#     # Convert the input matrix into a DataFrame
#     df = pd.DataFrame(input_matrix, index=names, columns=days)
    
#     st.subheader("Activity Data")
#     st.dataframe(df)
    
#     # Create heatmap using seaborn with specified color map for binary data
#     fig, ax = plt.subplots()
#     # Custom colormap: red for 0, green for 1
#     cmap = sns.color_palette(["red", "green"])
#     sns.heatmap(df, annot=True, cmap=cmap, cbar=True, ax=ax, fmt="d", cbar_kws={"ticks": [0, 1]})
#     ax.set_title("Weekly Activity Heatmap", pad=12)
    
#     # Render the plot in Streamlit
#     st.pyplot(fig)


# import streamlit as st
# import pandas as pd
# import numpy as np
# import seaborn as sns
# import matplotlib.pyplot as plt

# # Set page title
# st.title("Weekly Activity Heatmap")

# # Define names and weekdays
# names = ["Alice", "Bob", "Charlie", "Dave", "Eve"]
# days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

# # Create a form to capture the activity (0 or 1) for each person/day
# with st.form("admin_form"):
#     st.subheader("Enter Activity Status (0 or 1)")
    
#     # Prepare a matrix (list of lists) to hold the input
#     input_matrix = []
    
#     for name in names:
#         row_input = []
#         st.markdown(f"**{name}'s status**:")
#         cols = st.columns(len(days))
#         for i, day in enumerate(days):
#             # For each day, create a selectbox with options 0 or 1
#             value = cols[i].selectbox(
#                 f"{day}", 
#                 options=[0, 1], 
#                 key=f"{name}_{day}"
#             )
#             row_input.append(value)
#         input_matrix.append(row_input)
    
#     # Submit button
#     submitted = st.form_submit_button("Generate Heatmap")

# # Once the form is submitted, construct a DataFrame and display the heatmap
# if submitted:
#     # Convert the input matrix into a DataFrame
#     df = pd.DataFrame(input_matrix, index=names, columns=days)
    
#     st.subheader("Activity Data")
#     st.dataframe(df)
    
#     # Create heatmap using seaborn with specified color map for binary data
#     fig, ax = plt.subplots()
#     # Custom colormap: red for 0, green for 1
#     cmap = sns.color_palette(["red", "green"])
#     sns.heatmap(df, annot=True, cmap=cmap, cbar=True, ax=ax, fmt="d", cbar_kws={"ticks": [0, 1]})
#     ax.set_title("Weekly Activity Heatmap", pad=12)
    
#     # Render the plot in Streamlit
#     st.pyplot(fig)

# # import streamlit as st
# # import pandas as pd
# # import numpy as np
# # import seaborn as sns
# # import matplotlib.pyplot as plt

# # # Set page title
# # st.title("Weekly Activity Heatmap")

# # # Define names and weekdays
# # names = ["Alice", "Bob", "Charlie", "Dave", "Eve"]
# # days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

# # # Create a form to capture the activity (0 or 1) for each person/day
# # with st.form("admin_form"):
# #     st.subheader("Enter Activity Status (0 or 1)")
    
# #     # Prepare a matrix (list of lists) to hold the input
# #     input_matrix = []
    
# #     for name in names:
# #         row_input = []
# #         st.markdown(f"**{name}'s status**:")
# #         cols = st.columns(len(days))
# #         for i, day in enumerate(days):
# #             # For each day, create a selectbox with options 0 or 1
# #             value = cols[i].selectbox(
# #                 f"{day}", 
# #                 options=[0, 1], 
# #                 key=f"{name}_{day}"
# #             )
# #             row_input.append(value)
# #         input_matrix.append(row_input)
    
# #     # Submit button
# #     submitted = st.form_submit_button("Generate Heatmap")

# # # Once the form is submitted, construct a DataFrame and display the heatmap
# # if submitted:
# #     # Convert the input matrix into a DataFrame
# #     df = pd.DataFrame(input_matrix, index=names, columns=days)
    
# #     st.subheader("Activity Data")
# #     st.dataframe(df)
    
# #     # Create heatmap using seablit aorn
# #     fig, ax = plt.subplots()
# #     sns.heatmap(df, annot=True, cmap="YlGnBu", cbar=True, ax=ax)
# #     ax.set_title("Weekly Activity Heatmap", pad=12)
    
# #     # Render the plot in Streamlit
# #     st.pyplot(fig)
