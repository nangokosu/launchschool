def prompt(message):
    return f"=>{message}"

def invalid_number(number_str):
    try:
        int(number_str)
    except ValueError:
        return True

    return False



if __name__ == "__main__":
    print("Welcome to the calculator!")
    print(prompt("What's the first number? "))
    number1 = input()
    while invalid_number(number1):
        print("Not valid number")
        number1 = input()
    print(prompt("What's the second number? "))
    number2 = input()
    while invalid_number(number2):
        print("Not valid number")
        number2 = input()
    print('What operation would you like to perform?\n1) Add 2) Subtract 3) Multiply 4) Divide')
    operation = input()
    while operation not in ["1", "2", "3", "4"]:
        print(prompt('You must choose 1, 2, 3, or 4'))
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