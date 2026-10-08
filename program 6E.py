import pandas as pd
p = pd.Period('2026-01', freq='M')
print(p.asfreq('D', how='start'))
print(p.asfreq('D', how='end'))
period_index = pd.period_range(
    start='2026-01',
    periods=3,
    freq='M'
)
print(period_index.asfreq('D', how='start'))
print(period_index.asfreq('D', how='end'))