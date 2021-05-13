print("Welcome to tip calculator!")

total=float(input("Enter the total bill amount : $"))
per=int(input("How much percentage of bill you want to give ? (5%, 10%, 12%, 15%) : "))
people=int(input("How many people to split the bill : "))

bill_tip=total*(per/100)
split_amount=float((bill_tip+total)/people)
final_bill=round(split_amount,2)
print(f"Each person should pay : ${final_bill}")