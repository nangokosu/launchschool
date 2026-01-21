import random

VALID_CHOICES = ['rock','paper','scissors']

def prompt(message):
    return f"==> {message}"

if __name__ == "__main__":

    while True:
        print(prompt("Welcome to Rock Paper Scissors!"))
        player_choice = input(prompt(f"Make your choice between {', '.join(VALID_CHOICES)}: "))

        while player_choice.lower() not in VALID_CHOICES:
            print(prompt("Invalid choice, please check your grammar."))
            player_choice = input(prompt(f"Make your choice between {', '.join(VALID_CHOICES)}: "))

        
        
        computer_choice = VALID_CHOICES[random.choice([0,1,2])]

        print(prompt(f"You chose {player_choice}, computer chose {computer_choice}"))

        if player_choice == computer_choice:
            print("Draw!")
        elif((player_choice == "rock" and computer_choice == "scissors") or
        (player_choice == "paper" and computer_choice == "rock") or
        (player_choice == "scissors" and computer_choice == "paper")):
            print(prompt("You win!"))
        
        else:
            print(prompt("You lose!"))
        
        answer = input(prompt("Do you want to play again (y/n)? "))
        while answer.lower() not in ['y','n']:
             print(prompt("Invalid answer, please try again"))
             answer = input(prompt("Do you want to play again (y/n)? "))

        
        
        
        if 'n' in answer.lower():
            break

