from fastapi import FastAPI, HTTPException
import pandas as pd
import json
from pathlib import Path
from .backtest import backtest

app = FastAPI(title="Crypto Quant System")

DATA_DIR = Path(__file__).parent / "data"


@app.get("/coins")
def get_coins():
    with open(DATA_DIR / "coins.json") as f:
        return json.load(f)


@app.post("/backtest/{symbol}")
def run_backtest(symbol: str):
    file = DATA_DIR / f"{symbol.lower()}.csv"
    if not file.exists():
        raise HTTPException(status_code=404, detail="Data not found")
    df = pd.read_csv(file, parse_dates=["date"])
    result = backtest(df)
    return {
        "equity": result["equity_curve"].iloc[-1],
        "data": result.to_dict(orient="records"),
    }
