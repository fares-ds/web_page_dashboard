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
        return pd.read_csv(uploaded_file)
    
    df = load_csv()
    st.header("**Input DataFrame**")

    # Select Tickers
    tickers = df["Ticker"].unique().tolist()
    # st.write(tickers)
    selected_ticker = st.sidebar.multiselect("Primary Tickers", tickers, tickers)
    
    # Select Column
    columns = df.columns.tolist()
    selected_columns = st.sidebar.multiselect("Columns", columns, columns)
    print(selected_columns)
    st.write(df.loc[df["Ticker"].isin(selected_ticker), selected_columns])
else:
    st.info("Awaiting for CSV file to be uploaded.")


    