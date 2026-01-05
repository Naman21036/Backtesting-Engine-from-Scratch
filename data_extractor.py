
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import FunctionTransformer
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
import seaborn as sns
import pandas as pd
import yfinance as yf
def extract_stock_data(ticker, start_date, end_date):
    stock_data = yf.download(ticker, start=start_date, end=end_date)
    df= pd.DataFrame(stock_data)
    return df
def feature_engineering(df):
    df['Returns'] = df['Close'].pct_change()
    for col in df.columns:
        if df[col].isnull().sum()>0:
                df[col]= df[col].ffill().bfill()
    return df
def dump_to_csv(ticker,df):
    df.to_csv(f"{ticker}_ohlcv_report.csv")


def make_data_pipeline(ticker, start_date, end_date):
    def _extract(X):
        return extract_stock_data(ticker, start_date, end_date)

    def _features(X):
        return feature_engineering(X)

    def _dump(X):
        return dump_to_csv(ticker,X)

    pipeline = Pipeline(steps=[
        ("extract_stock_data", FunctionTransformer(_extract)),
        ("feature_engineering", FunctionTransformer(_features)),
        ("dump_to_csv", FunctionTransformer(_dump)),
    ])
    return pipeline
