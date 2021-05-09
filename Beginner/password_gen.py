import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to python password generator.")
ui_numbers=int(input("How many numbers you want in your password : "))
ui_letters=int(input("How many letters you want : "))
ui_symbols=int(input("How many symbols you want : "))

passw = []

for nu in range(1,ui_numbers+1):
    passw+=random.choice(numbers)
for ch in range(1,ui_letters+1):
    passw.append(random.choice(letters))
for sy in range(1,ui_symbols+1):
    passw+=random.choice(symbols)

random.shuffle(passw)
final_pass=""
for i in passw:
    final_pass+=i
print(f"Your password is : {final_pass}")