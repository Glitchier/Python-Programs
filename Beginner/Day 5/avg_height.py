print("Average Height Calculator.")
stu_hieghts=input("Enter the students heights : ")
split_stu_hieght=stu_hieghts.split()
sum=0
print("Entered heights are :")
for i in split_stu_hieght:
    print(i)
    sum=sum+int(i)
k=0
for stu in split_stu_hieght:
    k=k+1
avg_height=sum/k
print(f"Average height is : {avg_height}")
