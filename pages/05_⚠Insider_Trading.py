import streamlit as st
from fi_pye.readers.fmp import Insiders


st.title("Insider Trading")
data = Insiders(apikey=st.secrets['FMP_TOKEN'])

ticker = st.text_input("Stock symbol", placeholder="AAPL")

insider_trading_tab, insider_roster_tab, insider_roster_stats_tab = st.tabs(
    ["Insider Trading", "Insider Roster", "Insider Roster Stats"]
)

if ticker:
    with insider_trading_tab:
        st.write(data.insider_trading(ticker))

    with insider_roster_tab:
        st.write(data.insider_roster(ticker))

    with insider_roster_stats_tab:
        st.write(data.insider_roster_stats(ticker))