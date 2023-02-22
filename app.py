#!/usr/bin/env python
# coding: utf-8

# In[8]:


import streamlit as st
import pandas as pd
import plotly.express as px

# Load data
df = pd.read_csv('a22-recrutement-analytics.csv', encoding="ISO-8859-1")

# Set up the app
st.set_page_config(page_title='A22 Recruitment Dashboard')

# Add a title to the page
st.title('Analytics Dashboard of Recruitment Cohorte A22')

# Allow the user to choose a program
program_chosen = st.selectbox("Choose program of interest:", df["Program"].unique())

# Filter the data based on the program chosen
df_program = df[df["Program"]==program_chosen]

# Add a histogram of math results
st.header("Math Results Histogram")
fig_hist = px.histogram(df_program, x="Math Result")
st.plotly_chart(fig_hist)

# Add a strip plot of math results by nationality
st.header("Math Results Strip Plot by Nationality")
fig_strip = px.strip(df_program, x="Math Result", y="Nationality")
st.plotly_chart(fig_strip)


# Add a sunburst plot of programs, nationalities, and cities
df_sburst = df_program[df_program["Mode"].isin(["Alternant","Traditional","SPOC"])]
st.header("Programs, Nationalities, and Cities Sunburst Plot")
fig_sunburst = px.sunburst(df_sburst, path=["Program", "Nationality", "City"])
st.plotly_chart(fig_sunburst)

# Add an ECDF plot of math results
st.header("Math Results ECDF")
fig_ecdf = px.ecdf(df_program, x="Math Result")
st.plotly_chart(fig_ecdf)

# Add a line plot of math results by date and gender
st.header("Math Results by Mode Line Plot")
fig_line = px.line(df_program, x="Mode", y="Math Result", markers=True)
st.plotly_chart(fig_line)


# In[ ]:




