
score = float(input("Enter the student's score (0–100): "))

if 90 <= score <= 100:
    grade = "Grade A"
elif 70 <= score < 90:
    grade = "Grade B"
elif 50 <= score < 70:
    grade = "Grade C"
elif 0 <= score < 50:
    grade = "Fail"
else:
    grade = "Invalid score entered"

# Display the result
print(f"Score: {score}")
print(f"Result: {grade}")
