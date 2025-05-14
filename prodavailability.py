# Product Availability Checker

# List of available products
inventory = ['pen', 'pencil', 'eraser']

# Get product name from the user
product = input("Enter the product name: ").strip().lower()

# Check availability
if product in inventory:
    print(f"{product.capitalize()} is available in the inventory.")
else:
    print(f"{product.capitalize()} is not available in the inventory.")
