# Quant Trading Backtester and Strategy Engine

A modular Python based quantitative trading framework designed for data ingestion, feature engineering, strategy generation, and backtesting with realistic transaction costs.

This project focuses on clean separation between data pipelines, trading logic, and evaluation metrics, similar to real world quant research workflows.

---

## Features

- Market data extraction using Yahoo Finance
- Feature engineering pipeline with missing value handling
- Pluggable trading strategies
- Vectorized backtesting engine
- Transaction cost modeling
- Performance metrics including Sharpe ratio and max drawdown
- CSV based reporting for research and analysis

---

## Project Architecture

Data → Features → Strategy → Positions → Backtest → Metrics

Each component is independent and reusable.

---

## File Overview

### data_extractor.py
Handles market data ingestion and preprocessing.

- Downloads OHLCV data
- Computes returns
- Handles missing values
- Supports sklearn style pipelines
- Exports clean datasets to CSV

---

### strategies.py
Contains trading strategy logic.

Currently implemented:
- Moving Average Crossover Strategy

Strategies output clean trading signals that can be easily swapped or extended.

---

### engine.py
Core backtesting engine.

Responsibilities:
- Strategy return calculation
- Transaction cost adjustment
- Equity curve generation
- Risk metrics computation

Metrics included:
- Total return
- Sharpe ratio
- Max drawdown
- Volatility
- Average daily return

---

### model_runner.py
Execution entry point.

- Fetches data
- Applies feature engineering
- Runs selected strategy
- Executes backtest
- Prints performance metrics

---

## Installation

Create a virtual environment and install dependencies.

```bash
pip install -r requirements.txt
