# ATM Withdrawal Check

# Get account balance and withdrawal amount from the user
balance = float(input("Enter your account balance: ₹"))
withdrawal = float(input("Enter withdrawal amount: ₹"))

# Check if withdrawal is allowed
if withdrawal <= balance and withdrawal % 100 == 0:
    print("Withdrawal approved.")
    balance -= withdrawal
    print(f"Remaining balance: ₹{balance:.2f}")
elif withdrawal > balance:
    print("Withdrawal denied: Insufficient balance.")
elif withdrawal % 100 != 0:
    print("Withdrawal denied: Amount must be a multiple of ₹100.")
