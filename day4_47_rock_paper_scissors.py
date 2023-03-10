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

#Write your code below this line 👇
u_choice = int(input("Type 0 for Rock \nType 1 for Paper \nType 2 for Scissors \nWhat do you choose? "))

options = ['0', '1', '2']
c_choice = random.choices(options)
c_choice = int(c_choice[0])

if u_choice > 3 or u_choice < 0:
    print(f"I am sorry but {u_choice} is a invalid number. Try again.")
elif u_choice == c_choice:
  print("You guys have a Draw!!")
elif u_choice == 0:
  if c_choice == 1:
    print("\nYOU:", rock, "\nCPU:", paper)
    print("Computer wins! You Lose!")
  elif c_choice == 0:
    print("\nYOU:", rock, "\nCPU:", scissors)
    print("You win! Computer Loses!")
elif u_choice == 1:
    if c_choice == 0:
        print("\nYOU:", paper, "\nCPU:", rock)
        print("You win! Computer Loses!")
    if c_choice == 2:
        print("\nYOU:", paper, "\nCPU:", scissors)
        print("You Lose! Computer Wins!")
elif u_choice == 2:
    if c_choice == 0:
        print("\nYOU:", scissors, "\nCPU:", rock)
        print("You Lose! Computer Wins!")
    if c_choice == 1:
        print("\nYOU:", scissors, "\nCPU:", paper)
        print("You Win! Computer Loses!")