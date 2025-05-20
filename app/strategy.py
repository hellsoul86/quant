import pandas as pd
from .indicators import ema, rsi, bollinger_bands


def apply_indicators(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df['ema_fast'] = ema(df['close'], 12)
    df['ema_slow'] = ema(df['close'], 26)
    df['rsi'] = rsi(df['close'])
    ma, upper, lower = bollinger_bands(df['close'])
    df['bb_middle'] = ma
    df['bb_upper'] = upper
    df['bb_lower'] = lower
    return df


def generate_signals(df: pd.DataFrame) -> pd.DataFrame:
    """Generate long/flat signals based on indicators."""
    df = apply_indicators(df)
    df['signal'] = 0
    condition = (
        (df['close'] > df['bb_lower']) &
        (df['rsi'] < 30) &
        (df['ema_fast'] > df['ema_slow'])
    )
    df.loc[condition, 'signal'] = 1
    df['position'] = df['signal'].shift().fillna(0)
    return df
