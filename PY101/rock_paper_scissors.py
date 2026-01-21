import random

VALID_CHOICES = ['rock','paper','scissors']

ACRONYMS_MAPPING = {
    'r':'rock',
    'p':'paper',
    's':'scissors'
}

WINNING_COMBOS = {
    'rock': ['scissors'],
    'scissors': ['paper'],
    'paper': ['rock']

}


def _outcome(player_choice, computer_choice):
    if player_choice == computer_choice:
        print("Tie!")

    elif computer_choice in WINNING_COMBOS[player_choice]:
        print("You win!")
        global player_wins
        player_wins += 1

    else:
        print("You lose!")
        global computer_wins 
        computer_wins += 1


def prompt(message):
    return f"==> {message}"

if __name__ == "__main__":

    while True:
        print(prompt("Welcome to Rock Paper Scissors! best of 5"))

        player_wins = 0

        computer_wins = 0

        round_count = 1


        while max(player_wins,computer_wins)<3:
            print(prompt(f"Your wins: {player_wins}; Computer wins: {computer_wins}"))
            print(prompt(f"Round {round_count}"))
            player_choice = input(prompt(f"Make your choice between {', '.join(VALID_CHOICES)}: "))

            while player_choice.lower() not in VALID_CHOICES and ACRONYMS_MAPPING[player_choice.lower()[0]] not in VALID_CHOICES:
                print(prompt("Invalid choice, please check your grammar."))
                player_choice = input(prompt(f"Make your choice between {', '.join(VALID_CHOICES)}: "))

            player_choice = ACRONYMS_MAPPING[player_choice.lower()[0]]
            
            computer_choice = VALID_CHOICES[random.choice([0,1,2])]

            print(prompt(f"You chose {player_choice}, computer chose {computer_choice}"))

            
            _outcome(player_choice, computer_choice)

            round_count += 1
        
        if player_wins > computer_wins:
            print(prompt(f"You win, {player_wins}-{computer_wins}"))
        else:
            print(prompt(f"Computer win, {computer_wins}-{player_wins}"))
            
            
        answer = input(prompt("Do you want to play again (y/n)? "))
        while answer.lower() not in ['y','n']:
            print(prompt("Invalid answer, please try again"))
            answer = input(prompt("Do you want to play again (y/n)? "))

        if 'n' in answer.lower():
            break
        else:
            print("=====================================")

