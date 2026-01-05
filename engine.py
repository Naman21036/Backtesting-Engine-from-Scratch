import numpy as np
import pandas as pd


def compute_sharpe(returns: pd.Series, periods_per_year: int = 252) -> float:
    returns = returns.dropna()
    if returns.std(ddof=0) == 0:
        return 0.0
    return (returns.mean() * periods_per_year) / (
        returns.std(ddof=0) * np.sqrt(periods_per_year)
    )


def compute_max_drawdown(returns: pd.Series) -> float:
    equity = (1 + returns.fillna(0.0)).cumprod()
    running_max = equity.cummax()
    drawdown = equity / running_max - 1.0
    return drawdown.min()


def run_backtest(
    price,
    position,
    cost_per_unit: float = 0.0005,
    periods_per_year: int = 252,
) -> dict:

    # ---- FORCE 1D SERIES ----
    price = pd.Series(price.squeeze(), index=price.index).astype(float)
    position = pd.Series(position.squeeze(), index=price.index).fillna(0.0)

    # ---- RETURNS ----
    asset_returns = price.pct_change().fillna(0.0)

    # ---- STRATEGY RETURNS ----
    gross_returns = position * asset_returns

    # ---- TRANSACTION COSTS ----
    turnover = position.diff().abs().fillna(0.0)
    costs = turnover * cost_per_unit

    # ---- NET RETURNS ----
    net_returns = gross_returns - costs

    # ---- EQUITY CURVE ----
    equity_curve = (1 + net_returns).cumprod()

    metrics = {
        "total_return": equity_curve.iloc[-1] - 1.0,
        "sharpe_ratio": compute_sharpe(net_returns, periods_per_year),
        "max_drawdown": compute_max_drawdown(net_returns),
        "volatility": net_returns.std(ddof=0),
        "avg_daily_return": net_returns.mean(),
    }

    return {
        "returns": net_returns,
        "equity_curve": equity_curve,
        "metrics": metrics,
    }
