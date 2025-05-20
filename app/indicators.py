import pandas as pd


def ema(series: pd.Series, period: int) -> pd.Series:
    """Exponential moving average."""
    return series.ewm(span=period, adjust=False).mean()


def rsi(series: pd.Series, period: int = 14) -> pd.Series:
    """Relative strength index."""
    delta = series.diff()
    up = delta.clip(lower=0)
    down = -1 * delta.clip(upper=0)
    gain = up.ewm(com=period - 1, adjust=False).mean()
    loss = down.ewm(com=period - 1, adjust=False).mean()
    rs = gain / loss
    return 100 - (100 / (1 + rs))


def bollinger_bands(series: pd.Series, window: int = 20, num_std: int = 2):
    """Calculate Bollinger Bands."""
    ma = series.rolling(window=window).mean()
    std = series.rolling(window=window).std()
    upper = ma + num_std * std
    lower = ma - num_std * std
    return ma, upper, lower
