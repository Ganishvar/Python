x=int(input("Enter the number of elements in the Array "))
Num=[]
for i in range(0,x,1):
    y=int(input('Enter the numbers'))
    Num.append(y)
Max=0 
Min=Num[0]
for j in range(0,x,1):
    if(Max < Num[j]):
        Max=Num[j]
print(Max)
for j in range(0,x,1):
    if(Min > Num[j]):
        Min=Num[j]
print(Min)    