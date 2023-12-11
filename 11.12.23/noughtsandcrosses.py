# Data vals:
# -1 = O
# 0  = null
# 1  = X

def create_board():
    board = []
    for i in range(3):
        row = [0] * 3
        board.append(row)
    return board

def convert_to_letter(itm):
    if itm == -1:
        return "O"
    elif itm == 0:
        return " "
    elif itm == 1:
        return "X"
    else: raise Exception("[convert_to_letter]: Bad data")

def render_board(board):
    print()
    print(("+---" * 3) + "+")
    for row in board:
        letters = []
        for i in row:
            letters.append(convert_to_letter(i))
        print("| " + " | ".join(letters) + " |")
        print(("+---" * 3) + "+")

board = create_board()

print("Welcome to naughts and crosses!")
render_board(board)
