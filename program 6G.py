import pandas as pd
dates = pd.date_range(
    start='2026-01-01 00:00',
    periods=12,
    freq='h'
)
values = [10, 12, 15, 14, 18, 20,
          22, 21, 25, 28, 30, 32]
time_series = pd.Series(values, index=dates)
print(time_series.resample('3h').mean())
print(time_series.resample('4h').sum())
print(time_series.resample('30min').asfreq())
print(time_series.resample('30min').ffill())