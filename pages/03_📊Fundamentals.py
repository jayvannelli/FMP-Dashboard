import streamlit as st
from fi_pye.readers.fmp import Fundamentals


st.title("Stock Fundamentals")
data = Fundamentals(apikey=st.secrets['FMP_TOKEN'])

ticker = st.text_input("Stock symbol", placeholder="AAPL")

balance_sheet_tab, income_statement_tab, cash_flow_tab = st.tabs(
    ["Balance Sheet", "Income Statement", "Cash Flow"]
)

if ticker:
    with balance_sheet_tab:
        balance_sheet = data.balance_sheet(ticker)
        st.write(balance_sheet)

    with income_statement_tab:
        st.write(data.income_statement(ticker))

    with cash_flow_tab:
        st.write(data.cash_flow(ticker))
