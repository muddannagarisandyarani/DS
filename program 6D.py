import pandas as pd
p = pd.Period('2026-01', freq='M')
print(p)
print(p + 2)
print(p + 5)
print(p - 1)
print(p - 3)
periods = pd.period_range(
    start='2026-01',
    periods=6,
    freq='M'
)
print(periods)