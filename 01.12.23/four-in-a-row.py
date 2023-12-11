# https://missionencodeable.com/python/level/9/step/5

print("Welcome to Four in a Row!")
print()

player_chars = ["🔴", "🔵"]
player = 1

def init_board():
    board = []
    for i in range(6):
        row = ["⚪"] * 7
        board.append(row)
    return board

board = init_board()
print(len(board))

def render_board():
    print()
    print(("+----" * 7) + "+")
    for row in board:
        print('| ' + ' | '.join(row) + ' |')
        print(('+----' * 7) + "+")
    print("  1    2    3    4    5    6    7  ")

render_board()
