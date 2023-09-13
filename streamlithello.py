import streamlit as st

# Basic Streamlit Commands
st.title("Hello Streamlit")
st.header("This is a header")
st.subheader("This is a subheader")
st.markdown("**This** is a markdown")
st.code("print('Hello Streamlit')", language="python")
st.latex('''(a+b)^2 = a^2 + 2ab + b^2''')

# Button
if st.button("Click Me"):
    st.write("You clicked the button")
else:
    st.write("Please click the button")

# Input Text
data = st.text_input("Please enter data here")
if st.button("Submit"):
    st.write(f"Your data is {data}")

# Slider
score = st.slider(
    "Please enter your score", 
    min_value=0, 
    max_value=100, 
    value=10
)
st.write(f"Your score is {score}")