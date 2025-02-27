import pandas as pd
df = pd.DataFrame({'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [20, 25, 25]})
df_clean = df.dropna(subset=['Age'])

print(df_clean)