import math

def paint_cal(height,width,cover):
    area=height*width
    no_of_cans=math.ceil(area/cover)
    print(f"You will need {no_of_cans} cans of paint.")

test_h=int(input("Enter height of the wall : "))
test_w=int(input("Enter width of the wall : "))
coverage=6
paint_cal(height=test_h,width=test_w,cover=coverage)