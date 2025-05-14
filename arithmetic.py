# Arithmetic Operations Based on User Choice

# Get two numbers from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Get the operator from the user
operator = input("Enter an operator (+, -, *, /): ").strip()

# Perform the operation based on the operator
if operator == '+':
    result = num1 + num2
    operation = "Addition"
elif operator == '-':
    result = num1 - num2
    operation = "Subtraction"
elif operator == '*':
    result = num1 * num2
    operation = "Multiplication"
elif operator == '/':
    if num2 != 0:
        result = num1 / num2
        operation = "Division"
    else:
        result = None
        operation = "Division by zero is not allowed"
else:
    result = None
    operation = "Invalid operator"

# Display the result
if result is not None:
    print(f"{operation} result: {result}")
else:
    print(f"Error: {operation}")
