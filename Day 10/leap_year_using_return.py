def leap_year(year):
    if(year%4==0):
        if(year%100==0):
            if(year%400):
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def days_in_month(year,month):
    if(month<1 and month>12):
        print("Invalid Month!!!")
    month_days=[31,28,31,30,31,30,31,31,30,31,30,31]
    if leap_year(year) and month==2:
        return 29
    return (month_days[month-1])

ch=True
while ch:
    year=int(input("Enter Year : "))
    month=int(input("Enter month : "))
    days=days_in_month(year,month)
    print(days)
    choice=input("Try again ? Type yes or no : ").lower()
    if(choice=="no"):
        ch=False
        print("Thank You!")
