import random
from replit import clear
from art import cong_logo,guess_logo

def random_number_generator():
    ran_number=random.randint(1,101)
    return(ran_number)

def comp_fun(rand_number,lvl):
    k=0
    if(lvl=='easy'):
        attempt=10
    elif(lvl=='hard'):
        attempt=5
    while attempt>0:
        guess_number=int(input("Enter the number you guessed : "))
        if(guess_number==rand_number):
            clear()
            print(cong_logo)
            print(f"Yes you are right the number was {guess_number}")
            k=1
            attempt=0
        elif(guess_number<0 or guess_number > 100):
            clear()
            attempt-=1
            print(f"You guessed {guess_number} but the number is between 1 to 100. You have {attempt} attempt left.")
        elif(guess_number<rand_number):
            clear()
            attempt-=1
            print(f"You guessed {guess_number} which is low. You have {attempt} attempt left.")
        elif(guess_number>rand_number):
            clear()
            attempt-=1
            print(f"You guessed {guess_number} which is high. You have {attempt} attempt left.")
        else:
            print("Invalid Number!!")
    if(attempt==0 and k==0):
        clear()
        print("You loss!!")
        print(f"The number was : {rand_number}")

print(guess_logo)
play_agree=input("I'm guessing a number between 1 to 100. Do You wanna a guess that number ? Type 'y' or 'n'\n").lower().strip()
if(play_agree=='y'):
    diffi_lvl=input("Choose a difficulty level. Type 'easy' or 'hard'\n").lower().strip()
    if(diffi_lvl=='easy'):
        rand_number=random_number_generator()
        print("You have 10 attempts in easy difficulty.")
        comp_fun(rand_number,diffi_lvl)
            
    elif(diffi_lvl=='hard'):
        rand_number=random_number_generator()
        print("You have 5 attempts in hard difficulty.")
        comp_fun(rand_number,diffi_lvl)
    else:
        print("Invalid command.")
elif(play_agree=='n'):
    print("Bye!")
else:
    print("Invalid Command!!")