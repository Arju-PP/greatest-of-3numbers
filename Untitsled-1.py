import streamlit as st

st.write("Geatest Number selector among 3!")
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
a=st.number_input("Enter a")
b=st.number_input("Enter b")
c=st.number_input("Enter c")

st.subheader("The greatest Among the 3 Numbers is: ")
st.write(greatest(a,b,c))
