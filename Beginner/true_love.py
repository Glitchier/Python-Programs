print("Welcome to Love Calculator!")
name1=input("Enter your name : ")
name2=input("Enter your crush name : ")

com_name = name1 + name2
com_name_lower = com_name.lower()

t = com_name_lower.count("t")
r = com_name_lower.count("r")
u = com_name_lower.count("u")
e = com_name_lower.count("e")

true = t+r+u+e

l = com_name_lower.count("l")
o = com_name_lower.count("o")
v = com_name_lower.count("v")
e = com_name_lower.count("e")

love = l+o+v+e

total_score = str(true) + str(love)

total_score_int = int(total_score)

if(total_score_int <= 10 or total_score_int >= 90) :
    print(f"Your score is {total_score_int}, you are like + and -")
elif(total_score_int >= 40 and total_score_int <= 50):
    print(f"Your score is {total_score_int}, you are alright together.")
else :
    print(f"Your score is {total_score_int}.")