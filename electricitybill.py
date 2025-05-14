# Electricity Bill Calculator

# Get units consumed from the user
units = int(input("Enter the number of units consumed: "))

# Calculate bill based on slabs
if units <= 100:
    bill = units * 5
elif units <= 200:
    bill = (100 * 5) + ((units - 100) * 7)
else:
    bill = (100 * 5) + (100 * 7) + ((units - 200) * 10)

# Display the result
print(f"Total electricity bill for {units} units is: ₹{bill}")
