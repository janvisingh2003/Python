# Even/Odd and Multiple of 5 Classifier

num = int(input("Enter a number: "))

if num % 2 == 0 and num % 5 == 0:
    classification = "Even and divisible by 5"
elif num % 2 != 0 and num % 5 == 0:
    classification = "Odd and divisible by 5"
elif num % 2 == 0 and num % 5 != 0:
    classification = "Even and not divisible by 5"
else:
    classification = "Odd and not divisible by 5"

# Display the result
print(f"Number: {num}")
print(f"Classification: {classification}")
