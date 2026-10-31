import random

board = [' ' for x in range(10)]

def printBoard():
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('-----------')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('-----------')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')

def isWinner(bo, le):
    # Check all winning conditions
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or 
    (bo[4] == le and bo[5] == le and bo[6] == le) or
    (bo[1] == le and bo[2] == le and bo[3] == le) or
    (bo[1] == le and bo[4] == le and bo[7] == le) or
    (bo[2] == le and bo[5] == le and bo[8] == le) or
    (bo[3] == le and bo[6] == le and bo[9] == le) or
    (bo[1] == le and bo[5] == le and bo[9] == le) or
    (bo[3] == le and bo[5] == le and bo[7] == le))

def playerMove():
    run = True
    while run:
        move = input('Select a position to place an X (1-9): ')
        try:
            move = int(move)
            if move > 0 and move < 10:
                if board[move] == ' ':
                    run = False
                    board[move] = 'X'
                else:
                    print('Sorry, space is occupied!')
            else:
                print('Please type a number within the range!')
        except:
            print('Please type a number!')

def compMove():
    possibleMoves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    if possibleMoves:
        move = random.choice(possibleMoves) # random simple AI move
        board[move] = 'O'
        print('Computer placed an O in position', move)

def isBoardFull():
    return board.count(' ') <= 1

print('Welcome to Tic Tac Toe!')
printBoard()

while not(isBoardFull()):
    if not(isWinner(board, 'O')):
        playerMove()
        printBoard()
    else:
        print("Computer won!")
        break

    if not(isWinner(board, 'X')):
        compMove()
        if not(isBoardFull()):
            printBoard()
    else:
        print("You won!")
        break

if isBoardFull() and not isWinner(board, 'X') and not isWinner(board, 'O'):
    print("It's a Tie!")
