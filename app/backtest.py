import pandas as pd
from .strategy import generate_signals


def backtest(data: pd.DataFrame) -> pd.DataFrame:
    """Simple backtest assuming buy at open, sell at next open."""
    df = generate_signals(data)
    df['returns'] = data['close'].pct_change()
    df['strategy'] = df['position'] * df['returns']
    df['equity_curve'] = (1 + df['strategy']).cumprod()
    return df
