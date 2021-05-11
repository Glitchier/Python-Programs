import random

seed_person=int(input("Create a seed number : "))
random.seed(seed_person)

names=input("Give names separated with commas(,) : ")
names_split=names.split(",")

print("Names are :")
print(names_split)

len_names=len(names_split)

random_name=random.randint(0,len_names-1)

print(f"{names_split[random_name]} is going to pay the bill.")
