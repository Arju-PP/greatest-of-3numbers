import streamlit as st

st.write{"""
Geatest Number selector among 3
"""}
def greatest(a,b,c):
    if a>b:
        if a>c:
            return a
        else:
            return c
    else:
        if b>c:
            return b
        else:
            return c


st.header("Enter Numbers")
a=number_input("Enter a")
b=number_input("Enter b")
c=number_input("Enter c")
print("Greatest of 3 is :",greatest(a,b,c))
