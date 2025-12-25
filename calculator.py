if __name__ == "__main__":
    print("Welcome to the calculator!")
    number1 = input("What's the first number? ")
    number2 = input("What's the second number? ")
    print('What operation would you like to perform?\n1) Add 2) Subtract 3) Multiply 4) Divide')
    operation = input()


    if operation == '1':   # '1' represents addition
        output = int(number1) + int(number2)
    elif operation == '2': # '2' represents subtraction
        output = int(number1) - int(number2)
    elif operation == '3': # '3' represents multiplication
        output = int(number1) * int(number2)
    elif operation == '4': # '4' represents division
        output = int(number1) / int(number2)

    print(f"The result is: {output}")