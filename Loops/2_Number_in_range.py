for number in range(1,20,2):
    print(number)
totalstudents=int(input("Enter no of Students "))
Marks=[]
for i in range(0,totalstudents,1):
    mark=input("Enter your mark ")
    Marks.append(mark)
print(Marks)
for i in range(0,totalstudents,1):
    print('Student',i+1,'Marks are ',Marks[i])