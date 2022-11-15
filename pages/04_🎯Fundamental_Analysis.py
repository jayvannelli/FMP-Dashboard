import streamlit as st
from fi_pye.readers.fmp import FundamentalAnalysis


st.title("Stock Fundamental Analysis")
data = FundamentalAnalysis(apikey=st.secrets['FMP_TOKEN'])

ticker = st.text_input("Stock symbol", placeholder="AAPL")

if ticker:
    st.write(data.advanced_levered_dcf(ticker))
    st.write(data.advanced_dcf(ticker))
    st.write(data.discounted_cash_flow(ticker))