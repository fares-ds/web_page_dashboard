import numpy as np
import pandas as pd 
import streamlit as st 



# Web App Title
st.markdown('''
# **The EDA App**

This is a simple EDA app that has basic exploratory data analysis functionality like:
- Showing maximum and minimum based on certain `Ticker`
-  Show data in specific `Tichers` for a specific `Columns`
''')

# Reading The Data
with st.sidebar.header('1. Upload your CSV data'):
    uploaded_file = st.sidebar.file_uploader("Upload your input CSV file", type=["txt", "csv"])

if uploaded_file is not None:
    @st.cache
    def load_csv():
        return pd.read_csv(uploaded_file, sep=';')
    
    df = load_csv()
    st.header("**Input DataFrame**")
    # st.write(df)
else:
    st.info("Awaiting for CSV file to be uploaded.")

# Select Tickers
tickers = df["Ticker"].unique().tolist()
selected_ticker = st.sidebar.selectbox("Primary Tickers", tickers)
columns = df.columns.tolist()
selected_columns = st.sidebar.multiselect("Columns", columns)

st.write(df.loc[df["Ticker"] == selected_ticker, selected_columns])
    