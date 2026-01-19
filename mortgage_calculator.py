def prompt(message):
    return f"==>{message}"\

def invalid_number(str):
    try: 
        number = float(str)
        if number <= 0:
            raise ValueError("Value must be larger > 0")
    except ValueError:
        return True
    
    return False

def loan_duration():
    while True:
        print(prompt("What is the term duration for the loan in years? Only input numbers, and convert months to years e.g 18 months in 1.5 years"))
        num_of_years = input()
        while invalid_number(num_of_years):
            print(prompt("Invalid input, please follow the instructions and try again"))
            print(prompt("What is the term duration for the loan in years? Only input numbers, and convert months to years e.g 18 months is 1.5 years, and you input 1.5"))
            num_of_years = input()
        num_of_years_float = float(num_of_years)
        if num_of_years_float >= 12.0:
            print(prompt("Are you sure your loan durations is in years and not months? Y/N"))
            answer = input()
            if answer.lower() == 'y':
                break
            else:
                print(prompt("Invalid input, please follow the instructions and try again"))
        else:
            break
    
    return num_of_years_float






if __name__ == '__main__':

    print(prompt("Welcome to mortgage payment calculator"))
    print("----------------------------------")
    

    # input loan amount
    print(prompt("What is the loan amount?"))
    loan_amount = input()
    while invalid_number(loan_amount):
        print(prompt("Invalid input, please only input numbers with no commas"))
        print(prompt("What is the loan amount?"))
        loan_amount = input()

    # input APR:
    print(prompt("What is the APR? Input numbers: for X% APR, input X only"))
    apr = input()
    while invalid_number(apr):
        print(prompt("Invalid input, please follow the instructions and try again"))
        print(prompt("What is the APR? Input numbers: for X% APR, input X only"))
        apr = input()

    test_var = 1
    # input num_of_years:
    loan_duration_float = loan_duration()
    print(
        prompt(f"For a loan of ${loan_amount} for {loan_duration_float} years at {apr}% APR, your payment is {test_var}")
    )






        





    


    



    