# This program takes two numbers and an arithmetic operation (+, -, *, /) as input,
# then performs the selected operation and displays the result.
# It also handles division by zero by displaying an appropriate message.

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operation = input("Choose the operation (+, -, *, /): ")

match operation:
    case "+":
        print("The result is", num1 + num2)
    case "-":
        print("The result is", num1 - num2)
    case "*":
        print("The result is", num1 * num2)
    case "/":
        if num2 == 0:
            print("Cannot divide by 0")
        else:
            print("The result is", num1 / num2)
    case _:
        print("Invalid operation selected.")

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operation = input("Choose the operation (+, -, *, /): ")

match operation:
    case "+":
        print("The result is", num1 + num2)
    case "-":
        print("The result is", num1 - num2)
    case "*":
        print("The result is", num1 * num2)
    case "/":
        if num2 == 0:
            print("Cannot divide by 0")
        else:
            print("The result is", num1 / num2)
    case _:
        print("Invalid operation selected.")
