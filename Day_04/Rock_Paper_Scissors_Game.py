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
input_value=int(input("What do you choose?Type 0 for Rock,1 for Paper or 2 for Scissors:"))
input_actions=[rock,paper,scissors]
if input_value<0 or input_value>2:
    print("Invalid Choice")
    exit()
elif input_value==0:
    print(rock)
elif input_value==1:
    print(paper)
else:
    print(scissors)
computer_choice=random.choice(input_actions)
print(f"Computer Chose: \n + {computer_choice}")


if input_value==0 and computer_choice==rock:
    print("Game Tie")
elif input_value==1 and computer_choice == paper:
        print("Game Tie")
elif input_value==2 and computer_choice == scissors:
    print("Game Tie")
elif input_value==0 and computer_choice==scissors:
    print("You WIN!")
elif input_value==1 and computer_choice==rock:
    print("You WIN!")
elif input_value==2 and computer_choice == paper:
    print("You WIN!")
else:
    print("You LOSE")