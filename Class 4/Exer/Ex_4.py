P = float(input("Enter principal amount: "))
R = float(input("Enter rate of interest: ")) / 100
T = float(input("Enter the time in year: "))

interest = P*R*T
print(f"The simple interest is {interest:.2f}")