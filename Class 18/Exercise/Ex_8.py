import pandas as pd

df = pd.DataFrame({'Category': ['A', 'B', 'A', 'B'], 'Value': [10, 20, 15, 25]})

grouped = df.groupby('Category').sum()
print(grouped)