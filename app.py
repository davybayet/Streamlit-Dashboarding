#!/usr/bin/env python
# coding: utf-8

# In[8]:


import streamlit as st
import pandas as pd
import plotly.express as px

# Load data
df = pd.read_csv('all-cohorts-analytics.csv', encoding="ISO-8859-1")

# Set up the app
st.set_page_config(page_title='All Cohorts Recruitment Dashboard')

# Add a title to the page
st.title('Analytics Dashboard of Recruitment for all Cohortes')

# Allow the user to choose a program
program_chosen = st.selectbox("Choose program of interest:", df["Program"].unique())

# Filter the data based on the program chosen
df_program = df[df["Program"]==program_chosen]

# Add a histogram of math results
st.header("Birth Date Histogram")
fig_hist = px.histogram(df_program, x="Birth Date")
st.plotly_chart(fig_hist)

# Add a strip plot of math results by nationality
st.header("Birth Date Strip Plot by Nationality")
fig_strip = px.strip(df_program, x="Birth Date", y="Nationality")
st.plotly_chart(fig_strip)

# Add a pie plot of nationality by mode
st.header("Nationality by Mode Pie Plot")
fig_pie = px.pie(df_program, values="Birth Date", names="Nationality")
st.plotly_chart(fig_pie)

# Add a sunburst plot of programs, nationalities, and cities
df_sburst = df_program[df_program["Mode"].isin(["Alternant","Traditional","SPOC"])]
st.header("Programs, Nationalities Sunburst Plot")
fig_sunburst = px.sunburst(df_sburst, path=["Program", "Nationality"])
st.plotly_chart(fig_sunburst)

# Add an ECDF plot of math results
st.header("Birth Date-Yearly ECDF")
fig_ecdf = px.ecdf(df_program, x="Birth Date")
st.plotly_chart(fig_ecdf)

# Add a line plot of math results by date and gender
st.header("Birth Date-Yearly by Mode Line Plot")
fig_line = px.line(df_program, x="Mode", y="Birth Date", markers=True)
st.plotly_chart(fig_line)


# In[ ]:




