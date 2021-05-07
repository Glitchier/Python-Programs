import random

#using seed
random_seed=int(input("Create a seed : "))
random.seed(random_seed)

sides=random.randint(0,1)

if(sides==1):
    print("Heads")
else:
    print("Tails")

#normal
'''
ran=random.randint(0,1)
if(ran==1):
    print("heads")
else:
    print("tails")
'''