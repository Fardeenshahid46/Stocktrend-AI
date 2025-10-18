from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from features import add_features
import yfinance as yf
import joblib

def train_model(df):
    features=["Return","SMA_5","SMA_10","RSI"]
    X=df[features]
    y=df["Target"]
    X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,shuffle=False)
    model=RandomForestClassifier(n_estimators=100,random_state=42)
    model.fit(X_train,y_train)
    preds=model.predict(X_test)
    print(f"Accuracy:",accuracy_score(y_test,preds))
    joblib.dump(model,"model.pkl")
    return model

if __name__=="__main__":
    df=yf.download("AAPL","2020-01-01","2023-01-01")
    df=add_features(df)
    model=train_model(df)