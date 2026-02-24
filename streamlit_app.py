import streamlit as st
import pandas as pd

# لینک CSV گوگل شیت
url = "https://docs.google.com/spreadsheets/d/1Fm45mA7R8ysRLkLkpsoAY7omKGNhYLMPY6ktkwCPeUM/export?format=csv"

df = pd.read_csv(url)

st.title("Family Saving App")

st.dataframe(df)

st.header("Add New Entry")

name = st.text_input("Name")
amount = st.number_input("Amount", min_value=0)

if st.button("Submit"):
    st.success(f"Saved: {name} - {amount}")
