def calculator(a,b):
    add=a+b
    sub=a-b
    mul=a*b
    div=a/b
    mod=a%b
    return add,sub,mul,div,mod
x=float(input("Enter any number X "))
y=float(input("Enter any number Y "))
a,b,c,d,e=calculator(x,y)
print("Sum is ",a)
print("Difference is ",b)
print("Product is ",c)
print("Quotient is ",d)
print("Remainder is ",e)
