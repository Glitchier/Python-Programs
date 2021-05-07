row1=['🔲','🔲','🔲']
row2=['🔲','🔲','🔲']
row3=['🔲','🔲','🔲']

map=[row1,row2,row3]
print(f"{row1}\n{row2}\n{row3}")

print("Welcome to hide the treasure game!")
num=input("Where you want to hide your treasure (Ex : Column 1 & Row 2 as 12) : ")

hor=int(num[0])
ver=int(num[1])

sel_row=map[ver-1][hor-1]="❌"

print(f"{row1}\n{row2}\n{row3}")