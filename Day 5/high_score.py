stu_score=input("Enter student scores : ")
stu_score_split=stu_score.split()
for i in range(0,len(stu_score_split)-1) :
    stu_score_split[i]=int(stu_score_split[i])
high_score=0
for score in stu_score_split:
    if(int(score)>int(high_score)):
        high_score=score
print(f"Highest Score is : {high_score}") 