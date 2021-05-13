sum=0
for i in range(2,101,2):
    sum+=i
print(f"Sum of even numbers: {sum}")

sum=0
for i in range(1,101):
    if(i%2==0):
        sum+=i
print(f"Sum of even numbers: {sum}")