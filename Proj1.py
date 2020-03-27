#Tic Tac Toe
def display_board(board):
    print(board[1]+'|'+board[2]+'|'+board[3])
    print('- - -')
    print(board[4]+'|'+board[5]+'|'+board[6])
    print('- - -')
    print(board[7]+'|'+board[8]+'|'+board[9])
def position(player):
    if ' ' not in user_board:
        return None
    move=int(input('What position would you like to go to?'))
    while move>9 or move<1 or move is '':
        move=int(input('What position would you like to go to?'))
    while user_board[move] != ' ':
        move=int(input('What position would you like to go to?'))
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
    position(player2)
