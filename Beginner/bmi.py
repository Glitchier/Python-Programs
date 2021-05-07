height=float(input("Enter your height in meter(m) : "))
weight=float(input("Enter your weight in KG : "))
bmi=weight/(height*height)
print("Your BMI is : "+str(bmi))

if(bmi<=18.5):
    print("You are Underweight.")
elif(bmi>18.5 and bmi<=25):
    print("You have a Normal Weight.")
elif(bmi>25 and bmi<=30):
    print("You are Overweight.")
elif(bmi>30 and bmi<=35):
    print("You fall in category of Obese.")
elif(bmi>35):
    print("Clinically Obese, you need to see a Doctor.")
else:
    print("Invalid BMI!")