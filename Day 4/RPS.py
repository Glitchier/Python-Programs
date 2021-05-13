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

signs=[rock,paper,scissors]

print("Welcome to RPS game!")
choice=int(input("Enter 0 for Rock, 1 for Paper, 2 for Scissor : "))

cpu_choice=random.randint(0,2)

print(f"Your choice : {choice} {signs[choice]}")
print(f"Computer choice : {cpu_choice} {signs[cpu_choice]}")

if(choice==cpu_choice):
    print("Draw!")
elif(cpu_choice==0 and choice == 2):
    print("You Lose!")
elif(cpu_choice==2 and choice == 0):
    print("You Win!")
elif(cpu_choice > choice):
    print("You Lose!")
elif(cpu_choice < choice):
    print("You Win!")
else:
    print("Invalid Number!!!!")