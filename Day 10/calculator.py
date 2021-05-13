from replit import clear

def add(num1,num2):
    return (num1+num2)
def sub(num1,num2):
    return (num1-num2)
def mul(num1,num2):
    return (num1*num2)
def div(num1,num2):
    return (num1/num2)

operation={
    "+":add,
    "-":sub,
    "*":mul,
    "/":div
}

again=True

print('''
 _____________________
|  _________________  |
| | JO           0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|
''')
while again:
    num1=float(input("Enter the first number : "))
    num2=float(input("Enter the second number : "))

    for symbol in operation:
        print(symbol)
    operator=input("Enter the operation you want to do : ")

    if(operator=="+" or operator=="-" or operator=="*" or operator=="/"):
        fun_operation=operation[operator]
        ans=fun_operation(num1,num2)

        print(f"{num1} {operator} {num2} = {ans}")

        ch=input("Do you want to try again ? Type yes or no : ").lower().strip()
        if(ch=="no"):
            again=False
            clear()
            print("Thank You !")
        else:
            clear()
    else:
        print("Invalid Operator !!")