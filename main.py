import streamlit as st
import pandas as pd

st.write("## Heading")
st.write("This is my first streamlit app!")


# Text Inputs
st.write("## Text Inputs")
x = st.text_input("Enter Favourite Movie: ")
st.write(f"Your favourite movie is {x}")

# Buttons
st.write("## Buttons")
col1, col2 = st.columns(2)
clicked = col1.button("Click Me!")

col2.link_button("Profile", "/profile")

if clicked:
    st.write("Button Clicked")

# Showing Data (Tables and Graphs)
st.write("## Showing pandas DataFrame")
df = pd.read_csv("https://gist.githubusercontent.com/curran/a08a1080b88344b0c8a7/raw/0e7a9b0a5d22642a06d3d5b9bcbad9890c8ee534/iris.csv")
st.write(df.head())

st.write("## Charts")
st.bar_chart(df, x="species", y="petal_length")
st.scatter_chart(df,  x="petal_width", y=["petal_length", "sepal_length"])