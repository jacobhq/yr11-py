won = False
lost = False

# False is so
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
        return False

def check_won():
    global lost
    if chicken == grain and farmer != chicken:
        lost = True
        print("Chicken and grain left alone, chicken ate grain.")
    if fox == chicken and farmer != fox:
        lost = True
        print("Fox and chicken left alone, fox ate chicken.")


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
            chicken = not chicken
            farmer = not farmer
            check_won()
        case "grain":
            grain = not grain
            farmer = not farmer
            check_won()
        case _:
            print("Invalid choice, please choose either fox, chicken or grain")