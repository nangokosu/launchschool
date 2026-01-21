import json

with open('messages.json','r') as file:
    MESSAGES = json.load(file)






def prompt(message):
    return f"=>{message}"

def invalid_number(number_str):
    try:
        float(number_str)
    except ValueError:
        return True

    return False



if __name__ == "__main__":
    
    while True: 
        print(prompt(MESSAGES['welcome']))
        
        print(prompt(MESSAGES['first_prompt']))
        number1 = input()
        while invalid_number(number1):
            print("Not valid number")
            number1 = input()
        
        print(prompt(MESSAGES['second_prompt']))
        number2 = input()
        while invalid_number(number2):
            print("Not valid number")
            number2 = input()
            
        
        
        print(prompt(MESSAGES['third_prompt']))
        operation = input()
        while operation not in ["1", "2", "3", "4"]:
            print(prompt('You must choose 1, 2, 3, or 4'))
            operation = input()


        if operation == '1':   # '1' represents addition
            output = float(number1) + float(number2)
        elif operation == '2': # '2' represents subtraction
            output = float(number1) - float(number2)
        elif operation == '3': # '3' represents multiplication
            output = float(number1) * float(number2)
        elif operation == '4': # '4' represents division
            output = float(number1) / float(number2)

        print(f"The result is: {output}")
        print(prompt("Do you want another session? Y/N"))
        continue_choice = input()
        if continue_choice.lower() == 'n':
            break