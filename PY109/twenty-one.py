import random
import os

NUMBER = [str(number) for number in range(2,11)] + ['J','K','Q','A']
SUITE = ['Club','Spade','Heart','Diamond']

def shuffle(deck):
    random.shuffle(deck) # changes inplace

def prompt(statement):
    return f'=> {statement}'

def total(cards):
    # cards = [['H', '3'], ['S', 'Q'], ... ]
    values = [card[1] for card in cards]

    sum_val = 0
    for value in values:
        if value == "A":
            sum_val += 11
        elif value in ['J', 'Q', 'K']:
            sum_val += 10
        else:
            sum_val += int(value)

    # correct for Aces
    aces = values.count("A")
    while sum_val > 21 and aces:
        sum_val -= 10
        aces -= 1

    return sum_val

def print_hand(cards):
    values = [card[1] for card in cards]
    return ','.join(values[:-1]) + ' and ' + str(values[-1])

def print_both_hands(user, dealer):
    os.system('clear')
    print(prompt(f"Your hand: {print_hand(user)}"))
    print(prompt(f"Your hand value: {total(user)}"))
    print(prompt(f"Dealer hand: {print_hand(dealer)}"))
    print(prompt(f"Dealer hand value: {total(dealer)}"))



def twenty_one():
    deck = [[suite,number] for number in NUMBER for suite in SUITE]
    shuffle(deck)

    # Dealing initial hand
    
    dealer = []
    user = []

    user.append(deck.pop())
    dealer.append(deck.pop())
    user.append(deck.pop())
    dealer.append(deck.pop())
    print_both_hands(user,dealer)

    if total(user) == 21 and total(dealer) == 21:
        print(prompt("Draw!"))

    elif total(user) == 21:
        print(prompt("Blackjack!"))
        print(prompt("You win!"))
        return None
    
    elif total(dealer) == 21:
        print(prompt("Blackjack!"))
        print(prompt("Dealer win!"))
        return None
        


    cont = True

    ## user loop

    while cont:
        answer = str(input(prompt('Do you wish to hit? (y/n): ')))
        if answer == 'y':
            user.append(deck.pop())
            user_value = total(user)
            print_both_hands(user,dealer)
            
            
            
            if user_value > 21:
                print(prompt("Player Bust!"))
                return None

        elif answer == 'n':
            cont = False

    if total(user) <= 21:
    
        ## dealer loop

        dealer_value = total(dealer)

        while dealer_value < 17:
            dealer.append(deck.pop())
            dealer_value = total(dealer)
            print_both_hands(user,dealer)
    
        if dealer_value > 21:
            print(prompt("Dealer Bust!"))
            print(prompt("You win!"))
            

        elif dealer_value > total(user):
            print(prompt("Dealer win!"))
        elif dealer_value == total(user):
            print(prompt("Draw"))
        else:
            print(prompt("You win!"))
    
    
    else:
        print(prompt("You lose!"))
    
    return None


if __name__ == '__main__':
    twenty_one()

    next_game = input(prompt('Again? (y/n): '))

    while next_game == 'y':
        
        twenty_one()
        next_game = input(prompt('Again? (y/n): '))






        
        

    







    





