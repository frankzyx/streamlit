import streamlit as st
import pandas as pd

st.write("""
# My first app
Hello *world!*
""")

df = pd.read_csv('./apportionment.csv')
series = df[df['Geography Type'] == 'Nation']
series['Resident Population'] = pd.to_numeric(series['Resident Population'].str.replace(',', ''))
st.bar_chart(series, x='Year', y='Resident Population')
