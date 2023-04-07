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
game_image = [rock, paper, scissors]
user_choice = int(input("type 0 for rock,1 for paper and 2 for scissors\n"))
print(game_image[user_choice])
computer_choice = random.randint(0, 2)
print(f"computer choice is {computer_choice}")
print(game_image[computer_choice])
if user_choice == computer_choice:
    print("draw ")
elif user_choice == 0 and computer_choice == 1:
    print("computer won")
elif user_choice == 1 and computer_choice == 0:
    print("you won")
elif user_choice == 2 and computer_choice == 1:
    print("you won")
elif user_choice == 1 and computer_choice == 2:
    print("computer won")
elif user_choice == 0 and computer_choice == 2:
    print("you won")
elif user_choice == 2 and computer_choice == 0:
    print("computer won")
else:
    print("invaild number , try again")
