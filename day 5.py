import numpy as np
import altair as alt
import pandas as pd
import streamlit as st

st.header('st.write')

st.subheader('This is a subheader')


# Example 1

st.write('Hello, *World!* :sunglasses:')

# Example 2

st.write(1234)

# Example 3

df = pd.DataFrame({
     'first column': [1, 2, 3, 4],
     'second column': [10, 20, 30, 40]
     })
st.write(df)
st.caption('This is a table caption')

# Example 4

st.write('Below is a DataFrame:', df, 'Above is a dataframe.')

# Example 5

df2 = pd.DataFrame(
     np.random.randn(200, 3),
     columns=['a', 'b', 'c'])
c = alt.Chart(df2).mark_circle().encode(
     x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
st.write(c)

st.markdown('This is a markdown')

st.text('This is a random texts')

st.latex

st.code('sleep_for_a_minute <- function() { Sys.sleep(60) }')

st.code('end_time - start_time')
