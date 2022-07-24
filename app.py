import streamlit as st

st.write("""
# Two Numbler Multiplication App

This app multiplies two number
""")

st.header('User Input Parameters')

def user_input_features():
    n1 = st.number_input("Number_1")
    n2 = st.number_input("Number_2")

    return n1, n2

n1, n2 = user_input_features()
st.write(int(n1*n2))
