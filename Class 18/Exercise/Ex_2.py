import pandas as pd

df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'Dave'],
    'Age': [20, 25, 30, 35],
    'City': ['Dhaka', 'Khulna', 'Taylor', 'San Francisco']
})

print(df['City'])