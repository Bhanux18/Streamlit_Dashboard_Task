import streamlit as st

from matplotlib import image
import pandas as pd
import plotly.express as px
import os



st.title("iLab Data App !!")

st.subheader("Welcome to my online web app of  :red[Employee Data !] ")

btn1 = st.button("My Portfolio !")


if btn1 == True:
    #st.spinner("hurray")
    st.subheader("Hi Everyone !!")
    st.write("Myself :red[__Bhanuprakash__],an intern of Data Science at Innomatics Research Labs.I like to apply hands on experience utilizing domain knowledge of Statistics  with appropriate tools and techniques in solving the realtime problems hidden in the data.")
    st.write("\n")
    st.write("My very aim is to work with the [__Umbrella of Data Science__] disciplines.I can perform statistical analyses using R, Excel (Moderate)and then python,I'm willing to learn more about what I am capable of.")
    st.write("\n")
    st.write("\n")
    st.write("\n")

   
    st.write("Feel free to connect with me on below respective platform link")
    #btn2 = st.button("My Portfolio !")
    st.markdown("[Linkedin](https://www.linkedin.com/in/bhanux18/)")
    st.markdown("[Github](https://github.com/Bhanux18)")
    st.markdown("[mail-to](mailto:coursestuff25@gmail.com)")
    









    st.balloons()