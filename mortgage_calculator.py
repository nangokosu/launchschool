def prompt(message):
    return f"==>{message}"\

def invalid_number(str):
    try: 
        number = int(str)
        if number <= 0:
            raise ValueError("Value must be larger > 0")
    except ValueError:
        return True
    
    return False



if __name__ == '__main__':

    print(prompt("Welcome to mortgage payment calculator"))

    