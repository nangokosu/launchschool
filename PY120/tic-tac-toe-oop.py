import random
import os

class Player:
  def __init__(self, name, symbol = 'X'):
    self.symbol = symbol
    self.name = name

  def choose(self):
    row = int(input("What row do you want? (0-2): "))
    column = int(input("What column do you want? (0-2): "))
    return (row, column)


class ComputerPlayer(Player):
  def __init__(self, name):
    super().__init__(name = 'Computer', symbol = 'O')

  def choose(self):
    row = random.randint(0, 2)
    column = random.randint(0, 2)
    return (row, column)


class Board:
    def __init__(self):
        print("New Tic-Tac-Toe game")
        self.board = [
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' ']
        ]
        self.print_board()
        self.human_player = Player(name = 'Player 1')
        self.computer_player = ComputerPlayer(name = 'Computer')


    def print_board(self):
        for row in self.board:
            print("-----")
            print(f"{row[0]}|{row[1]}|{row[2]}")
        print("-----")
  

    def conduct_turn(self, player):
        os.system('clear')
        print(f"{player.name}'s turn")
        row, column = player.choose()
        while self.board[row][column] != ' ':
            if player.name != 'Computer':
                print("That space is already taken. Try again.")
            row, column = player.choose()
        self.board[row][column] = player.symbol
        self.print_board()
        
           
     
  
  
    def conduct_full_turn(self):
        
        self.conduct_turn(self.human_player)
        if self.check_win(self.human_player):
            print('You win!')
            return True
        
        self.conduct_turn(self.computer_player)
        if self.check_win(self.computer_player):
            print('Computer wins!')
            return True
        
        print("-------------------")
        return False
  
    def game(self):
        winner_found = False
        while not winner_found:
            winner_found = self.conduct_full_turn()
    

    def check_win(self, player):
        player = player.symbol


    # 1. Check Rows
        for row in self.board:
            if all(cell == player for cell in row):
                return True

    # 2. Check Columns
        for col in range(3):
            if all(self.board[row][col] == player for row in range(3)):
                return True

    # 3. Check Diagonals
    # Main diagonal (top-left to bottom-right)
        if all(self.board[i][i] == player for i in range(3)):
            return True
    
    # Anti-diagonal (top-right to bottom-left)
        if all(self.board[i][2 - i] == player for i in range(3)):
            return True

        return False
  

if __name__ == '__main__':
   while True:
    os.system("clear")
    board = Board()
    board.game()
    answer = input("Do you want to play again (y/n)? ")
    if answer.lower() == 'n':
       break




 