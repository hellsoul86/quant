import pandas as pd
from app.backtest import backtest


def test_backtest_runs():
    df = pd.DataFrame({
        'date': pd.date_range('2023-01-01', periods=5),
        'close': [1, 2, 3, 4, 5]
    })
    result = backtest(df)
    assert 'equity_curve' in result
