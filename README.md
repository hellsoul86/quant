# Crypto Quant System

This repository provides a minimal FastAPI application demonstrating a 
quantitative trading strategy using RSI, Bollinger Bands and EMA. 
A simple backtest engine is included for demonstration purposes.

## Features

- Top 50 cryptocurrency symbols stored in `app/data/coins.json`.
- Technical indicators implemented in `app/indicators.py`.
- Strategy and backtest logic in `app/strategy.py` and `app/backtest.py`.
- FastAPI routes defined in `app/main.py`.

## Usage

Install dependencies (FastAPI, pandas, etc.) and run:

```bash
uvicorn app.main:app --reload
```

Call `/coins` to view available symbols and `/backtest/{symbol}` to run a 
backtest using CSV data stored in `app/data/{symbol}.csv`.
