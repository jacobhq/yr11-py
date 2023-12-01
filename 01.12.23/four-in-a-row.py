# https://missionencodeable.com/python/level/9/step/5

print("Welcome to Four in a Row!")
print()

player_chars = ["🔴", "🔵"]
player = 1

def init():
    board = []
    for i in range(6):
        row = []