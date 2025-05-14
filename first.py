bill_amount = float(input("Enter the total bill amount (in ₹): "))
if bill_amount > 1000:
    discount = 0.20
elif bill_amount > 500:
    discount = 0.10
else:
    discount = 0.0


discount_amount = bill_amount * discount
final_amount = bill_amount - discount_amount

# Print the results
print(f"Original Bill Amount: ₹{bill_amount:.2f}")
print(f"Discount Applied: ₹{discount_amount:.2f}")
print(f"Final Amount to Pay: ₹{final_amount:.2f}")
