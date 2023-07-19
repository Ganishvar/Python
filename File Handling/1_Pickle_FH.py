import pickle
colors=['red','orange','blue','green']
x=7
y=3.14
names=['gani','ganishvar']
numbers=[1,2,3,4,5]
dataSet=[colors,x,y,names,numbers]
with open('mydata.pkl','wb') as f:
    pickle.dump(colors,f)
    pickle.dump(x,f)
    pickle.dump(names,f)
    pickle.dump(numbers,f)
    pickle.dump(dataSet,f)
with open('mydata.pkl','rb') as f2:
    a=pickle.load(f2)
    b=pickle.load(f2)
    c=pickle.load(f2)
    d=pickle.load(f2)
    e=pickle.load(f2)
print(a)
print(b)
print(c)
print(d)
print(e)
for dt in dataSet:
    print(dt)