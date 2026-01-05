import numpy as np
import pandas as pd

def moving_average_strategy(df, short_window=40, long_window=100):
    signals = pd.DataFrame(index=df.index)
    signals['signal'] = 0.0

    signals['short_mavg'] = df['Close'].rolling(short_window, min_periods=1).mean()
    signals['long_mavg'] = df['Close'].rolling(long_window, min_periods=1).mean()

    signals.loc[signals.index[short_window:], 'signal'] = np.where(
        signals['short_mavg'].iloc[short_window:] > signals['long_mavg'].iloc[short_window:],
        1.0,
        0.0
    )

    signals['signal'] = signals['signal'].shift(1).fillna(0.0)
    signals['positions'] = signals['signal'].diff()

    return signals
