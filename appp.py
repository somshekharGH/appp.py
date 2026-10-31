import streamlit as st
import yfinance as yf
import pandas as pd

st.title("Nifty50 Dashboard")
stocks = ["RELIANCE.NS","TCS.NS","INFY.NS","HDFCBANK.NS","ICICIBANK.NS","SBIN.NS","BHARTIARTL.NS","ITC.NS","LT.NS","AXISBANK.NS","KOTAKBANK.NS","BAJFINANCE.NS","MARUTI.NS","SUNPHARMA.NS","WIPRO.NS","ULTRACEMCO.NS","TITAN.NS","ONGC.NS","NTPC.NS","POWERGRID.NS","M&M.NS","TATASTEEL.NS","HCLTECH.NS","BAJAJFINSV.NS","ADANIENT.NS","ADANIPORTS.NS","ASIANPAINT.NS","NESTLEIND.NS","GRASIM.NS","JSWSTEEL.NS","HINDALCO.NS","CIPLA.NS","DRREDDY.NS","EICHERMOT.NS","BRITANNIA.NS","DIVISLAB.NS","HINDUNILVR.NS","SBILIFE.NS","HDFCLIFE.NS","COALINDIA.NS","BAJAJ-AUTO.NS","HEROMOTOCO.NS","INDUSINDBK.NS","TATAMOTORS.NS","TATACONSUM.NS","TECHM.NS","APOLLOHOSP.NS","BEL.NS","TRENT.NS"]

data = []
for s in stocks:
    try:
        h = yf.Ticker(s).history(period="2d")
        cmp = h['Close'].iloc[-1]
        prev = h['Close'].iloc[-2] if len(h)>1 else cmp
        chg = (cmp-prev)/prev*100
        data.append([s.replace(".NS",""), round(cmp,2), round(chg,2)])
    except:
        pass

df = pd.DataFrame(data, columns=["Stock","CMP","Change%"])
st.dataframe(df)
