import pandas as pd

def add_features(df):
    df["Return"]=df["Close"].pct_change()
    df["SMA_5"]=df["Close"].rolling(5).mean()
    df["SMA_10"]=df["Close"].rolling(10).mean()
    df["RSI"]=compute_rsi(df["Close"])
    df["Target"]=(df["Close"].shift(-1)>df["Close"]).astype(int)
    df.dropna(inplace=True)
    return df

def compute_rsi(series,window=14):
    delta=series.diff()
    up,down=delta.clip(lower=0),-delta.clip(upper=0)
    gain=up.rolling(window).mean()
    loss=down.rolling(window).mean()
    rs=gain/loss
    return 100-(100/(1+rs))