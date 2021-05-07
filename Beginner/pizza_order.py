print("Welcome to Python Pizza order!")
print("Small size(S) : $15.")
print("Medium size(M) : $20.")
print("Large size(L) : $25.")

size=input("Enter the size of pizza. (S, M, L) : ")
pep=input("Do you want to add pepperoni to your pizza? (Y, N) : ")
cheese=input("Do you want to add extra cheese to your pizza? (Y, N) : ")

bill=0

if(size=='S'):
    bill=15
elif(size=='M'):
    bill=20
elif(size):
    bill=25
else:
    print("Invalid input!")

if(pep=='Y'):
    print("Pepperoni for Small pizza : +$2")
    print("Pepperoni for Medium pizza and Large pizza : +$3")
    if(size=='S'):
        bill=bill+2
    elif(size=='M' or size=='L'):
        bill=bill+3
else:
    print("No Pepperoni!")

if(cheese=='Y'):
    print("Extra cheese for Small pizza : +$1")
    print("Extra cheese for Medium pizza and Large pizza : +$2")
    if(size=='S'):
        bill=bill+1
    elif(size=='M' or size=='L'):
        bill=bill+2
else:
    print("No Extra cheese!")

print(f"Your final Bill is : {bill}")
print("Thanks for ordering.")