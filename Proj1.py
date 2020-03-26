#Tic Tac Toe
def display_board(board):
    print(board[1]+'|'+board[2]+'|'+board[3])
    print('- - -')
    print(board[4]+'|'+board[5]+'|'+board[6])
    print('- - -')
    print(board[7]+'|'+board[8]+'|'+board[9])

user_board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']

player1=input('Player 1! Please choose X or O')
while player1 not in 'OXxo':
    player1=input('Please choose X or O')
print('{1}{2}{3}\n{4}{5}{6}\n{7}{8}{9}')

if player1 is 'X':
    player2 is 'O'
elif player1 is 'O':
    player2 is 'X'

move=int(input('What position would you like to go to?'))
while move>9 or move<1 or move is '':
    move=int(input('What position would you like to go to?'))

def input1(example):
    player1=user_board[example]
    return display_board(user_board)
print(input1(move))
