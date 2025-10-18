import yfinance as yf
import pandas as pd
import os

def fetch_data(ticker="AAPL", period="1mo"):
    # Fetch stock data from Yahoo Finance
    df = yf.download(ticker, period=period)
    
    # Ensure data folder exists
    os.makedirs("data", exist_ok=True)
    
    # Save as CSV
    file_path = f"data/{ticker}.csv"
    df.to_csv(file_path)
    print(f"✅ Data for {ticker} saved successfully at: {file_path}")
    print(df.tail())  # Show last few rows
    return df

if __name__ == "__main__":
    fetch_data("AAPL", "1mo")
