import random

NUMBER = list(range(2,11)) + ['J','K','Q','A']
SUITE = ['Club','Spade','Heart','Diamond']

def shuffle(deck):
    random.shuffle(deck) # changes inplace

def prompt(statement):
    return f'=>{statement}'



if __name__ == '__main__':
    deck = [f'{number}-{suite}' for number in NUMBER for suite in suite]
    shuffle(deck)

    # Dealing initial hand
    
    dealer = []
    user = []

    user.append(deck.pop())
    dealer.append(deck.pop())
    user.append(deck.pop())
    dealer.append(deck.pop())

    answer = str(input(prompt('Do you wish to hit? (y/n): ')))






    





