import pandas as pd
from app.indicators import ema, rsi, bollinger_bands


def test_ema():
    s = pd.Series([1, 2, 3, 4, 5])
    result = ema(s, 3)
    assert len(result) == 5
    assert result.iloc[-1] > 0


def test_rsi():
    s = pd.Series([1, 2, 3, 2, 1, 2, 3])
    result = rsi(s, 2)
    assert len(result) == 7


def test_bollinger():
    s = pd.Series(range(20))
    ma, upper, lower = bollinger_bands(s)
    assert len(ma) == len(upper) == len(lower) == 20
