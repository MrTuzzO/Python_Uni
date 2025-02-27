import pandas as pd

df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'Dave'],
    'Age': [20, 25, 30, 35],
    'Salary': [100, 200, 300, 400]
})
df['Gender'] = ['M', 'F', 'M', 'F']
print(df)