import pandas as pd

df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'Dave'],
    'Salary': [50000, 60000, 70000, 80000],
    'Gender': ['Male', 'Female', 'Male', 'Female'],
})

mean_salary =df.groupby('Gender')['Salary'].mean()
print(mean_salary)