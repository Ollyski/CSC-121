while True:
    try:
        num1 = input("Enter the first number: ")
        num1 = int(num1)
        break  
    except ValueError:
        print("Please enter a valid number.")

while True:
    try:
        num2 = input("Enter the second number: ")
        num2 = int(num2)
        break  
    except ValueError:
        print("Please enter a valid number.")

result = num1 + num2

print(f"The sum of {num1} and {num2} is: {result}")