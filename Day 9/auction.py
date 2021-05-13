from art import logo
from replit import clear
print(logo)

bid_dic={}
run_again=True

def high_bid(bid_dic_record):
    high_amount=0
    winner=""
    for bidder in bid_dic_record:
        bid_amount=bid_dic_record[bidder]
        if(bid_amount>high_amount):
            high_amount=bid_amount
            winner=bidder
    print(f"The winner is {winner} with a bid of ${high_amount}")
print("The auction start's here .....")

while(run_again):
    key_name=input("Enter your name : ")
    key_value=float(input("Enter your bid : $"))
    bid_dic[key_name]=key_value
    run_again_ch=input("Is there any another bidder? Type Yes or No\n").lower()
    if(run_again_ch=="no"):
        run_again=False
        high_bid(bid_dic)
    elif(run_again_ch=="yes"):
        clear()