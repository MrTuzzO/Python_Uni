import pandas as pd
data = pd.read_csv('employees_large.csv')

avg_salary_by_dept = data.groupby("Department")["Salary"].mean()

highest_avg_salary_dept = avg_salary_by_dept.idxmax()

print("Average salary by department:\n", avg_salary_by_dept)
print("\nDepartment with highest average salary:", highest_avg_salary_dept)