import streamlit as st
import pandas as pd

df = pd.DataFrame({
    'Name': ["Alice","Bob","Charlie"],
    'Age': [23,67,69],
    'City': ["Podujeva","Prishtina",'Drenas']
})


st.write(df)