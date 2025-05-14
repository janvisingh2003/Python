# Divisibility Check

# Get the number from the user
num = int(input("Enter a number: "))

# Check divisibility
if num % 3 == 0 and num % 5 == 0:
    result = "Divisible by both 3 and 5"
elif num % 3 == 0:
    result = "Divisible only by 3"
elif num % 5 == 0:
    result = "Divisible only by 5"
else:
    result = "Not divisible by 3 or 5"

# Display the result
print(f"Number: {num}")
print(f"Result: {result}")
