won = False
lost = False

# False is south
grain = False
fox = False
farmer = False
chicken = False

print("A fox, chicken and a bag of grain wait by the side of a river.")
print("Left alone without you, the fox would eat the chicken and the chicken would eat the grain.")
print("Which item will you take in your rowboat to the other side? (fox, chicken, grain)")

def is_move_valid(item):
    if item == farmer:
        return True
    else:
        print("You must be on the same side as the item you wish to move. Try again!")
        return False

def check_won():
    global lost
    global won
    if chicken == grain and farmer != chicken:
        lost = True
        print("You lose! Chicken and grain were left alone, so the chicken ate the grain.")
    if fox == chicken and farmer != fox:
        lost = True
        print("You lose! Fox and chicken were left alone, so the fox ate the chicken.")
    if chicken == farmer == fox == grain == True:
        won = True
        print("Congratulations, you win!")

# Main loop
while won != True and lost != True:
    choice = input("Choice: ")
    # Switch case, invert variable
    match choice:
        case "fox":
            if is_move_valid(fox) == False:
                break
            fox = not fox
            farmer = not farmer
            check_won()
        case "chicken":
            if is_move_valid(chicken) == False:
                break
            chicken = not chicken
            farmer = not farmer
            check_won()
        case "grain":
            if is_move_valid(grain) == False:
                break
            grain = not grain
            farmer = not farmer
            check_won()
        case "":
            farmer = not farmer
            check_won()
        case _:
            print("Invalid choice, please choose either fox, chicken or grain")