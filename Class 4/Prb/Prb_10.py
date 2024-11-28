balance = 0

while True:
    print("\nSimple Banking System")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = int(input("Choose an option: "))

    if choice == 1:
        print("Your balance is:", balance)
    elif choice == 2:
        deposit = float(input("Enter amount to deposit: "))
        balance += deposit
        print("Deposit successful. Your new balance is:", balance)
    elif choice == 3:
        withdrawal = float(input("Enter amount to withdraw: "))
        if withdrawal <= balance:
            balance -= withdrawal
            print("Withdrawal successful. Your new balance is:", balance)
        else:
            print("Insufficient balance.")
    elif choice == 4:
        print("Exited....")
        break
    else:
        print("Invalid option. Please try again.")