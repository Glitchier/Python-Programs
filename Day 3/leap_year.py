print("Welcome to Leap Year Checker!")
year=int(input("Enter the year you want to check : "))
if(year%4==0 and year%100==0 and year%400==0):
    print(f"{year} is Leap year.")
else:
    print(f"{year} is not Leap year.")