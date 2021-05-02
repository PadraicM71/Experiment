
EMPTY_SIGN = '.'
AI_SIGN = 'X'# as in our gamr ai always gose first
OPPONENT_SIGN = 'O'

board = ['.','.','.','.','.','.','.','.','.']

def print_board(board):
    print(" ")
    print(' '.join(board[:3]))
    print(' '.join(board[3:6]))
    print(' '.join(board[6:]))
    print(" ")

print_board(board)

# print(board[:index] + 'O' + board[index+1:])

def all_moves_from_board(board, sign):  # if empty square return positions of empty squares
     move_list = []
     for i, v in enumerate(board):
         if v == EMPTY_SIGN:
             move_list.append(board[:i] + sign + board[i+1:])
     return move_list

all_moves_from_board(board, AI_SIGN)


