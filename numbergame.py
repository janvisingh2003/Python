# Number Comparison Game

# Get two numbers from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Compare the numbers
if num1 > num2:
    result = f"{num1} is greater than {num2}"
elif num2 > num1:
    result = f"{num2} is greater than {num1}"
else:
    result = "Both numbers are equal"

# Display the result
print(result)
