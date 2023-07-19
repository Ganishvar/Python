import pickle
names=[]
grades=[]
x=int(input('Enter the number of Students '))
i=0
for i in range(i,x,1):
    name=input('Enter your name ')
    names.append(name)
    print(name,',','Enter your Grade')
    grade=input()
    grades.append(grade)
with open('Grades.pkl','wb') as data:
    pickle.dump(x,data)
    pickle.dump(names,data)
    pickle.dump(grades,data)
with open('Grades.pkl','rb') as dataread:
    a=pickle.load(dataread)
    b=pickle.load(dataread)
    c=pickle.load(dataread)
print(a)
print(b)
print(c)

