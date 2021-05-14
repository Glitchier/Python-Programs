import random
import math
from replit import clear

cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]

def cards_sum():
    computer_total=0
    user_total=0
    for i in range(len(computer_cards)):
        computer_total+=computer_cards[i]
    for i in range(len(user_cards)):
        user_total+=user_cards[i]
    print(f"Computer cards are : {computer_cards}")
    print(f"User cards are : {user_cards}")
    print(f"Computer Total : {computer_total}")
    print(f"Your Total : {user_total}")
    if(computer_total<17):
        clear()
        print("Since computer cards total are smaller than 17, computer redraws card.")
        computer_ran_card=random.choice(cards)
        computer_cards.append(computer_ran_card)
        for i in range(len(computer_cards)):
            computer_total+=computer_cards[i]
        cards_sum()
    elif(computer_total>21 and user_total>21):
        print("Draw")
    elif(computer_total==user_total):
        print("Draw")
    elif(computer_total>21):
        print("You win!")
    elif(user_total>21):
        print("You lose!")
    elif(user_total>computer_total):
        print("You win!")
    elif(user_total<computer_total):
        print("You lose!")
    else:
        print("Error!!")

play_again=True
clear()
while play_again:
    user_cards=[]
    computer_cards=[]
    want_to_play=input("Do you want to play a game of Blackjack? Type 'y' or 'n' : ").lower().strip()
    if(want_to_play=='y'):
        print("""
                 _     _            _    _            _    
                | |   | |          | |  (_)          | |   
                | |__ | | __ _  ___| | ___  __ _  ___| | __
                | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
                | |_) | | (_| | (__|   <| | (_| | (__|   < 
                |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
                                       _/ |                
                                      |__/                 
            """)
        for i in range(1,3):
            computer_ran_card=random.choice(cards)
            computer_cards.append(computer_ran_card)
        print(f"Computer first card is {computer_cards[0]}")
        for i in range(1,3):
            user_ran_card=random.choice(cards)
            user_cards.append(user_ran_card)
        print(f"Your cards are : {user_cards}")
        draw_again_while=True
        while(draw_again_while):
            draw_again=input("Do you want to draw again ('y' or 'n') : ").lower().strip()
            if(draw_again=='y'):
                clear()
                user_ran_card=random.choice(cards)
                user_cards.append(user_ran_card)
                print(f"Your cards are : {user_cards}")
            else:
                draw_again_while=False
        if(draw_again=='n'):
            clear()
            cards_sum()
    else:
        play_again=False
        clear()
        print("Bye!")