import streamlit as st
import pandas as pd
import joblib
import os

st.title("📊 StockTrend AI — Apple (AAPL) Stock Prediction")

# Load trained model
model_path = os.path.join("src", "model.pkl")
model = joblib.load(model_path)

# Load CSV data (adjust path if needed)
csv_path = os.path.join("data", "AAPL.csv")
df = pd.read_csv(csv_path, header=[0, 1], index_col=0)

# Flatten MultiIndex columns (e.g., ('Close', 'AAPL') → 'Close')
df.columns = [col[0] for col in df.columns]

# Display dataframe preview
st.subheader("Recent Stock Data (AAPL)")
st.dataframe(df.head())

#Plot closing price
st.subheader("📈 AAPL Closing Price Trend")
st.line_chart(df["Close"])

