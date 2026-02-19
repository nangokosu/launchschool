import random
import os

INITIAL_MARKER = ' '
HUMAN_MARKER = 'X'
COMPUTER_MARKER = '0'

def display_board(board):
    os.system('clear')
    print('')
    print('')
    print('     |     |')
    print(f"  {board[1]}  |  {board[2]}  |  {board[3]}")
    print('     |     |')
    print('-----+-----+-----')
    print('     |     |')
    print(f"  {board[4]}  |  {board[5]}  |  {board[6]}")
    print('     |     |')
    print('-----+-----+-----')
    print('     |     |')
    print(f"  {board[7]}  |  {board[8]}  |  {board[9]}")
    print('     |     |')
    print('')
   #code omitted




def initialize_board():
    return {square: INITIAL_MARKER for square in range(1, 10)}

def prompt(message):
    return f'==> {message}'


def player_chooses_square(board):
    empty_squares = [key for key,value in board.items() if value == INITIAL_MARKER]
    user_choice = int(input(prompt("Choose a square (1-9): ")))
    valid_choice = False
    while not valid_choice:
        if user_choice in empty_squares:
            valid_choice = True
        elif user_choice in board.keys():
            user_choice = int(input(prompt("Square taken. Choose a square (1-9): ")))
        else:
            user_choice = int(input(prompt("Invalid input. Choose a square (1-9): ")))
        
    board[int(user_choice)] = HUMAN_MARKER

def computer_chooses_square(board):
    empty_squares = [key for key,value in board.items() if value == INITIAL_MARKER]
    choice = random.choice(empty_squares)
    board[choice] = COMPUTER_MARKER





def detect_winner(board):
    winning_lines = [
        [1, 2, 3], [4, 5, 6], [7, 8, 9],  # rows
        [1, 4, 7], [2, 5, 8], [3, 6, 9],  # columns
        [1, 5, 9], [3, 5, 7]              # diagonals
    ]

    for line in winning_lines:
        sq1, sq2, sq3 = line
        if (board[sq1] == HUMAN_MARKER
               and board[sq2] == HUMAN_MARKER
               and board[sq3] == HUMAN_MARKER):
            return 'Player'
        elif (board[sq1] == COMPUTER_MARKER
                  and board[sq2] == COMPUTER_MARKER
                  and board[sq3] == COMPUTER_MARKER):
            return 'Computer'

    return None

def full_board(board):
    empty_squares = [key for key,value in board.items() if value == INITIAL_MARKER]
    return empty_squares 


def tic_tac_toe():
    board = initialize_board()
    
    
    display_board(board)

    while True:

        player_chooses_square(board)
        display_board(board)

        if detect_winner(board):
            
            print(prompt(detect_winner(board) + ' wins!'))
            break

        if not full_board(board):
            
            print(prompt("No one wins :("))
            break
        
        computer_chooses_square(board)
        display_board(board)

        if detect_winner(board):
           
            print(prompt(detect_winner(board) + ' wins!'))
            break

        if not full_board(board):
            
            print(prompt("No one wins :("))
            break

        


       
    
    return None


    




if __name__ == '__main__':
    tic_tac_toe()

    while True:
        answer = str(input(prompt("Do you want to play again (y/n): ")))
        if answer.lower() == 'n':
            break
        tic_tac_toe() 


    


    


    
