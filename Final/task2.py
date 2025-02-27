import pandas as pd

sales_df = pd.read_csv("sales_large.csv")

total_sales = sales_df.groupby(["Region", "Product"])["Sales"].sum()

highest_sales_product = sales_df.groupby("Product")["Sales"].sum().idxmax()

print("Total sales by product in each region:\n", total_sales)
print("\nProduct with highest total sales:", highest_sales_product)
