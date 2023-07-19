mycolor=input("Enter your color ")
if(mycolor=='red' or mycolor=='Red' or mycolor=='RED'):
    print('Red is your color')
else:
    print('Youre color is not Red')
num=float(input('Enter your number '))
if(num%2==0):
    print("Your number is even")
if(num%2==1 and num<100):
    print('Your number is odd')