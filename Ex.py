
EMPTY_SIGN = '.'
AI_SIGN = 'X'# as in our gamr ai always gose first
OPPONENT_SIGN = 'O'

board = "........."
board1 = EMPTY_SIGN*9
print(board)
print(board1)
print (type(board))
print (type(board1))


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

a=all_moves_from_board(board, AI_SIGN)
print(a)


empty_cell_count = sum(1 for cell in board if cell == EMPTY_SIGN)


print(empty_cell_count)


def all_moves_from_board_list(board_list, sign):
    move_list = []
    for board in board_list:
        move_list.extend(all_moves_from_board(board, sign))
    return move_list

print(all_moves_from_board_list([EMPTY_SIGN * 9 ], AI_SIGN))
print(all_moves_from_board_list([board], AI_SIGN))


