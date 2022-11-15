import streamlit as st
from fi_pye.readers.fmp import Senators


st.title("Senate Trading")
data = Senators(apikey=st.secrets['FMP_TOKEN'])


ticker = st.text_input("Stock symbol", placeholder="AAPL")

if ticker:
    st.write(data.senate_trading(symbol=ticker))