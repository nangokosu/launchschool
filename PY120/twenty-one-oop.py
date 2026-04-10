import random
import os

class Player:
    def __init__(self, name):
        self.name = name
        self.cards = []

    def hand_total(self):
        values = [card[1] for card in self.cards]

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
    
    def print_hands(self):
        os.system("clear")
        values = [card[1] for card in self.cards]
        hand_text =  ', '.join(values[:-1]) + ' and ' + str(values[-1])
        print(f"==> {self.name}'s hand: {hand_text}")
        print(f"==> {self.name}'s value: {self.hand_total()}")
    

    def draw(self, deck):
        self.cards.append(deck.pop())


    def game_loop(self, deck):
        while True: 
            if self.check_condition():
                break

            answer = str(input('==> Do you wish to hit? (y/n): '))
            if answer == 'y':
                os.system("clear")
                self.draw(deck)
                user_value = self.hand_total()
                self.print_hands()
            elif answer == 'n':
                break
    
    def check_condition(self):
        value = self.hand_total()
        if value > 21:
            print(f"==> {self.name} is bust!")
            return True
        elif value == 21:
            print(f"==> {self.name} has Blackjack!")
            return True
        
        return False
        
    
class Dealer(Player):
    def __init__(self):
        super().__init__("Dealer")
    
    def game_loop(self, deck, threshold):
        dealer_value = self.hand_total()
        while dealer_value < 17:
            self.draw(deck)
            self.print_hands()
            dealer_value = self.hand_total()



class Deck:
    
    def __init__(self):
    
        self.NUMBER = [str(number) for number in range(2,11)] + ['J','K','Q','A']
        self.SUITE = ['Club','Spade','Heart','Diamond']
        self.deck = [[suite,number] for number in self.NUMBER for suite in self.SUITE]

    def shuffle(self):
        random.shuffle(self.deck)

    def pop(self):
        return self.deck.pop()


class Game:
    def __init__(self, player, dealer):
        self.deck = Deck()
        self.deck.shuffle()
        self.player = player
        self.dealer = dealer


        for i in range(0,2):
            self.player.draw(self.deck)
            self.dealer.draw(self.deck)
        
        self.player.print_hands()
        self.dealer.print_hands()

        self.print_all_hands()
    
    def print_all_hands(self):
        self.player.print_hands()
        self.dealer.print_hands()

    def check_condition(self, actor):
        value = actor.hand_total()
        if value > 21:
            print(f"==> {actor.name} is bust!")
            return True
        elif value == 21:
            print(f"==> {actor.name} has Blackjack!")
            return True
        
        return False
    
    def final_results(self, actor, dealer):
        if actor.hand_total() > dealer.hand_total():
            print(f"==> {actor.name} wins!")        
        elif actor.hand_total() < dealer.hand_total():
            print(f"==> {dealer.name} wins!")  
        else:
            print("Draw")


    
    def full_game_loop(self):
        
        # checking blackjack in first hand
        if self.player.check_condition() or self.dealer.check_condition():
            return 
        
        # If not blackjack, game continues

        self.player.game_loop(self.deck)
        self.print_all_hands()
        if self.player.check_condition():
            return

        self.dealer.game_loop(self.deck, 17)
        self.print_all_hands()
        if self.dealer.check_condition():
            return 
        
        self.final_results(self.player, self.dealer)
        

        




if __name__ == '__main__':
    while True:
        os.system("clear")
        player1 = Player("player1")
        dealer = Dealer()
        game = Game(player1, dealer)
        game.full_game_loop()
        answer = input("Do you want to play again (y/n)? ")
        if answer.lower() == 'n':
            break

    




    


    



