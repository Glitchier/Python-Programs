from art import logo,vs
from data import data
import random
from replit import clear

def format_data(account):
    acc_name=account["name"]
    acc_dis=account["description"]
    acc_country=account["country"]
    return f"{acc_name}, a {acc_dis} from {acc_country}"

clear()
score=0
print(logo)

user_right=True
while user_right:
    rand_ch_1=random.choice(data)
    rand_ch_2=random.choice(data)
    if(rand_ch_1==rand_ch_2):
        rand_ch_2=random.choice(data)
    print(f"Compare A : {format_data(rand_ch_1)}")
    print(vs)
    print(f"Against B : {format_data(rand_ch_2)}")

    guess=input("Who has more followers ? Type 'A' or 'B' : ").lower().strip()

    if(guess=='a'):
        if(rand_ch_1['follower_count']>rand_ch_2['follower_count']):
            clear()
            print(f"Yes you are right {rand_ch_1['name']} has more followers.")
            score+=1
            print(f"Your score : {score}")
        else:
            clear()
            print(f"Sorry you are wrong {rand_ch_2['name']} has more followers.")
            print(f"Your final score : {score}")
            user_right=False
    elif(guess=='b'):
        if(rand_ch_2['follower_count']>rand_ch_1['follower_count']):
            clear()
            print(f"Yes you are right {rand_ch_2['name']} has more followers.")
            score+=1
            print(f"Your score : {score}")
        else:
            clear()
            print(f"Sorry you are wrong {rand_ch_1['name']} has more followers.")
            user_right=False
            print(f"Your final score : {score}")
    else:
        print("Choose A or B.")