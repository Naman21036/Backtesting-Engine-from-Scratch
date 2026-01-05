from data_extractor import extract_stock_data, feature_engineering
from strategies import moving_average_strategy
from engine import run_backtest

df = feature_engineering(
    extract_stock_data("TSLA", "2020-01-01", "2023-01-01")
)

signals = moving_average_strategy(df)

position = signals["signal"].reindex(df.index).fillna(0.0)

result = run_backtest(df["Close"], position)

print(result["metrics"])
