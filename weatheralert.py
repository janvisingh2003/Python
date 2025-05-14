# Weather Alert System

# Get temperature input from the user
temperature = float(input("Enter the temperature in °C: "))

# Determine the weather alert
if temperature > 40:
    alert = "Heat Alert"
elif temperature > 30:
    alert = "Warm"
else:
    alert = "Normal"

# Display the alert
print(f"Temperature: {temperature}°C")
print(f"Weather Alert: {alert}")
