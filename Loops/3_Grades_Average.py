totalstudents=int(input("Enter no of Students "))
Marks=[]
sum=0
for i in range(0,totalstudents,1):
    mark=input("Enter your mark ")
    Marks.append(mark)
    sum=sum+float(Marks[i])
    Average=sum/totalstudents
print('Avg Marks',Average)
for i in range(0,totalstudents,1):
    print('Student',i+1,'Marks are ',Marks[i])