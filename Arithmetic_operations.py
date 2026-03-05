# Take two numbers from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Perform arithmetic operations
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2

# Division-related operations (handle divide-by-zero safely)
if num2 != 0:
    division = num1 / num2
    floor_division = num1//num2
else:
    print("Division (num1 / num2): Not possible (cannot divide by zero)")

power = num1 ** num2

# Print results with clear labels
print("\n--- Results ---")
print(f"Addition (num1 + num2): {addition}")
print(f"Subtraction (num1 - num2): {subtraction}")
print(f"Multiplication (num1 * num2): {multiplication}")

if num2 != 0:
    print(f"Division (num1 / num2): {division}")
    print(f"Floor Division (num1 // num2): {floor_division}")

print(f"Power (num1 ** num2): {power}")
