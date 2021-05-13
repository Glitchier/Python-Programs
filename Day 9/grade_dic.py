student_score={
    "Harry":85,
    "Ron":78,
    "Harmione":99,
    "Draco":59
}
for i in student_score:
    print(f"{i} : {student_score[i]}")
print("-----------------------------------------")
print("------------- Grades are ----------------")
print("-----------------------------------------")
for key in student_score:
    if(student_score[key] > 90 and student_score[key] <= 100):
        print(f"{key} : Outstanding")
    elif(student_score[key] > 80 and student_score[key] <= 90):
        print(f"{key} : Exceeds Expectations")
    elif(student_score[key] > 70 and student_score[key] <= 80):
        print(f"{key} : Acceptable")
    elif(student_score[key] < 70):
        print(f"{key} : Fail")
    else:
        print(f"{key} : No Data")