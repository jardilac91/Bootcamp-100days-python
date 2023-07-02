logo = '''
 _                                     _     _                 _ 
| |                                   (_)   | |               | |
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
| __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
| |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|

'''
print(logo)

print("Welcome to Treasure Island.\nYour mission is to find the treasure")

choice_1 = input("You\'re at a crossroad, where do you want to go?\nType 'left' or 'right': ").lower()

if choice_1 == 'left':
    choice_2 = input("You\'ve come to a lake, there is an island in the middle of the lake.\nType 'wait' to wait for a boat or Type 'swim' to swim across: ").lower()
    if choice_2 == 'wait':
        choice_3 = input("You arrive at the island. There is a house with three doors. One red, one yellow and one blue.\nWhich colour do you choose? ").lower()
        if choice_3 == "yellow":
            print("You found the treasure!")
        elif choice_3 == "red":
            print("It\'s a room full of fire.\nGame Over.")
        elif choice_3 == "blue":
            print("There are beasts in the room who eaten You.\nGame Over.")
        else: 
            print("That door doesn't exists.\nGame Over.")
    else:
        print("You got attacked by a trout.\nGame Over.")
else:
    print("You fell into a hole.\nGame Over.")
