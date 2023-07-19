A=[]
def Arraysum(index,array):
    total=0
    for i in range(0,index,1):  
        total=total+array[i]
    return total
index=int(input("Enter the total number of elements in array"))
for j in range(0,index,1):
    n=int(input("Enter any number"))
    A.append(n)
Sum=Arraysum(index,A)
print(Sum)