import streamlit as st
from matplotlib import image
import pandas as pd
import plotly.express as px
import os

# absolute path to  file
file_dir = os.path.dirname(os.path.abspath(__file__))
# absolute path of root directory
parent_dir = os.path.join(file_dir, os.pardir)
# absolute path of directory
dir = os.path.join(parent_dir, "resources")

path_image = os.path.join(dir, "images", "4565.jpg")
path_data = os.path.join(dir, "data", "Employee.csv")

st.title("Employee Data -Dashboard")

img = image.imread(path_image)
st.image(img)

st.write("Dataframe of :red[__Employee data__] ")
df = pd.read_csv(path_data)
st.dataframe(df)

dim=df.describe()
st.write("Summary statistics of dataframe :blue[__df__] ")
st.dataframe(dim)

department = st.selectbox("Select the Departments:", df['department'].unique())

col1, col2 = st.columns(2)

fig_1 = px.line(df[df['department'] == department], x="Gross_Salary", title='Highest Gross salary index')
col1.plotly_chart(fig_1, use_container_width=True)

fig_2 = px.box(df[df['department'] == department], y="salary")
col2.plotly_chart(fig_2, use_container_width=True)

cou = st.selectbox("Select the country for :red[__salary__] count for each employee:", df['country'].unique())
#col3 = st.column(1)
fig_3 = px.scatter(df[df['country'] == cou], x="salary")
st.plotly_chart(fig_3, use_container_width=True)

st.text("No.of employee in each country :")
fig = px.histogram(df, x="country", category_orders=df[df['country'] == cou])
st.plotly_chart(fig, use_container_width=True)

# Gender and educ Attributes

gen = st.radio("Select the Gender:", df['gender'].unique())
fig_4= px.pie(df[df['gender'] == gen], values='educ', names='educ', title='Rate of employees based on education qualifications')
st.plotly_chart(fig_4, use_container_width=False)

st.text("Gross salary comparision for gender by job category :")
fig5 = px.scatter(df, x="Gross_Salary", y="jobcat", color="gender")
st.plotly_chart(fig5, use_container_width=False)

#Performance by gender
st.text("Gross salary visualization based on performance by gender :")
fig6= px.box(df, x="Performance", y="Gross_Salary", color="gender")
st.plotly_chart(fig6, use_container_width=False)

st.write("\n")
st.write("\n")
st.write("\n")
st.write("\n")
st.write("\n")
st.write("\n")




st.caption("__Created By:__  _Bhanuprakash_,Data Science Intern @ :red[__Innomatics Research Labs__]")