import pickle
with open('Grades.pkl','rb') as d:
    n=pickle.load(d)
    student=pickle.load(d)
    marks=pickle.load(d)
print(n)
print(student)
print(marks)
while(1==1):
    name=input("What is the name of the Student")
    for i in range(0,n,1):
        if (student[i]==name):
            print(name,"You grade is",marks[i])