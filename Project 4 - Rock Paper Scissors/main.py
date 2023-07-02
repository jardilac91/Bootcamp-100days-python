import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images= [rock, paper, scissors]

user_choice = int(input("What do you choose?\nType 0 For Rock, 1 for Paper o 2 for Scissors: "))

if user_choice >= 3 or user_choice < 0:
    print("You enter an invalid number. Game Over.")
else: 
    print(f"User chose:\n {game_images[user_choice]}")


computer_choice = random.randint(0,2)
print(f"Computer chose:\n {game_images[computer_choice]}")

if user_choice == 0 and computer_choice == 2:
    print("You win! :D")
elif computer_choice == 0 and user_choice == 2:
    print("You lose :(")
elif computer_choice < user_choice:
    print("You Win! :D")
elif user_choice < computer_choice:
    print("You lose :(")
elif user_choice == computer_choice:
    print("It\'s a draw")


