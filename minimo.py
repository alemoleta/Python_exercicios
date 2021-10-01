# 3.1.1.9 Tomar decisões em Python

# Read three numbers.
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))

# Check which one of the numbers is the smallest
# and pass it to the smallest_number variable.

smallest_number = min(number1, number2, number3)

# Print the result.
print("The smallest number is:", smallest_number)
