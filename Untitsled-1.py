import streamlit as st

st.header("Geatest Number selector among 3!")
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


st.subheader("Enter Numbers")
a=st.number_input("Enter a",step=1)
b=st.number_input("Enter b",step=1)
c=st.number_input("Enter c",step=1)


st.write("The greatest Among the 3 Numbers is: ",greatest(a,b,c))
