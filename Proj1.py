#Tic Tac Toe
def display_board(board):
    print(board[1]+'|'+board[2]+'|'+board[3])
    print('- - -')
    print(board[4]+'|'+board[5]+'|'+board[6])
    print('- - -')
    print(board[7]+'|'+board[8]+'|'+board[9])

def win(player):
    if user_board[4]==player and user_board[5]==player and user_board[6]==player:
        return True
    elif user_board[1]==player and user_board[2]==player and user_board[3]==player:
        return True
    elif user_board[7]==player and user_board[8]==player and user_board[9]==player:
        return True
    elif user_board[1]==player and user_board[4]==player and user_board[7]==player:
        return True
    elif user_board[2]==player and user_board[5]==player and user_board[8]==player:
        return True
    elif user_board[3]==player and user_board[6]==player and user_board[9]==player:
        return True
    elif user_board[1]==player and user_board[5]==player and user_board[9]==player:
        return True
    elif user_board[3]==player and user_board[5]==player and user_board[7]==player:
        return True
    else:
        return False

def position(player):
    if ' ' not in user_board:
        return None
    while True:
        move=int(input('What position would you like to go to?'))
        if move>9 or move<1 or move is '':
            pass
        elif user_board[move] != ' ':
            pass
        else:
            break
    user_board[move]=player
    return display_board(user_board)

example_board=['#','1','2','3','4','5','6','7','8','9']
user_board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']

#game start
player1=input('Player 1 Please choose X or O')
while player1 not in 'OXxo':
    player1=input('Please choose X or O')

display_board(example_board)

player2=None
if player1 in 'Xx':
    player2 = 'O'
else:
    player2 = 'X'
player1=player1.upper()

while ' ' in user_board:
    position(player1)
    if win(player1)==True:
        print('You Won!')
        break
    position(player2)
    if win(player2)==True:
        print('You Won!')
        break
if ' ' not in user_board:
    print('It was a tie!')
