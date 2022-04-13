import streamlit as st
from datetime import time, datetime
import pandas as pd
import numpy as np


st.write("----------------------------------------------- Day 9 Challenge --------------------------------------------------")

st.header('Line chart')

chart_data = pd.DataFrame(
     np.random.randn(200, 5),
     columns=['a', 'b', 'c'])

st.dataframe(chart_data)

st.line_chart(chart_data)









st.write("----------------------------------------------- Day 8 --------------------------------------------------")



st.header('st.slider')

# Example 1

st.subheader('Slider')

age = st.slider('How old are you?', 0, 130, 25)
st.write("I'm ", age, 'years old')

# Example 2

st.subheader('Range slider')

values = st.slider(
     'Select a range of values',
     0.0, 100.0, (25.0, 75.0))
st.write('Values:', values)

# Example 3

st.subheader('Range time slider')

appointment = st.slider(
     "Schedule your appointment:",
     value=(time(11, 30), time(12, 45)))
st.write("You're scheduled for:", appointment)

# Example 4

st.subheader('Datetime slider')

start_time = st.slider(
     "When do you start?",
     value=datetime(2020, 1, 1, 9, 30),
     format="MM/DD/YY - hh:mm")
st.write("Start time:", start_time)
