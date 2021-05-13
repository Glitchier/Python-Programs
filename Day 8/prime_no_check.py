def prime_check(num):
    is_prime=True
    for i in range(2,num-1):
        if(num%i==0):
            is_prime=False
    if(is_prime):
        print(f"{num} is prime number.")
    else:
        print(f"{num} is not prime number.")

num=int(input("Enter your number : "))
prime_check(num)