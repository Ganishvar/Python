j=1
while(j<5):
    j=j+.1
    j=round(j,1)
    print(j)

n=int(input('Enter the number of students'))
i=0
j=0
Mark=[]
while(i<n):
    x=input("Enter your Mark")
    Mark.append(x)
    i=i+1

while(j<n):
    print(Mark[j])
    j=j+1