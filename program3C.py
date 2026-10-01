import numpy as np
import pandas as pd
data = pd.DataFrame(np.random.randn(100, 3))
outliers = (data > 3) | (data < -3)
print(outliers.sum())