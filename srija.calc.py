def calc(a,b,c):
    if(c=='+'):
        return(a+b)
    elif(c=='-'):
        return(a-b)
    elif(c=='*'):
        return(a*b)
    else:
        return(a/b)

y=int(input())
x=int(input())
h=input("enter any of the four(+,-,*,/)")
k=calc(y,x,h)
print(k)

               
