print("Warning : This is thing apply for 90 years only!")
age=input("Enter your age :\n")
final_age=90-int(age)
no_days=int(final_age)*365
no_weeks=int(final_age)*52
no_months=int(final_age)*12
print(f"You have {no_days} days, {no_weeks} weeks and {no_months} months left")