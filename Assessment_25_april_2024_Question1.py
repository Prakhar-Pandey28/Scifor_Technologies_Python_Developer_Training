def input_no(func):
    def wrapper():
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        return func(num1, num2)
    return wrapper

def calculator(func):
    def wrapper(num1, num2):
        return func(num1, num2)
    return wrapper

@input_no
@calculator
def add(num1, num2):
    return num1 + num2

@input_no
@calculator
def subtract(num1, num2):
    return num1 - num2

@input_no
@calculator
def multiply(num1, num2):
    return num1 * num2

@input_no
@calculator
def divide(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        return "Error: Division by zero!"

while True:
    print("\nSelect operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("Enter choice (1/2/3/4/5): ")

    if choice == '5':
        break
    elif choice in ('1', '2', '3', '4'):
        operation = add if choice == '1' else subtract if choice == '2' else multiply if choice == '3' else divide
        print("Result:", operation())
    else:
        print("Invalid input")