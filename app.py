import pandas as pd
import streamlit as st
url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQeuVfY863gm7T-IWzy6mcBmgnjOSLs5WlxoTqtzt1DvWOMWHuueX9A-roSe5u2fm5yPZZW0yVPzsu4/pub?gid=0&single=true&output=csv"
df = pd.read_csv(url)
st.title("Monitoramento IoT")
st.line_chart(df[['temperatura', 'umidade']])
st.dataframe(df)
