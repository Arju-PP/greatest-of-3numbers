def greatest(a,b,c):
    if a>b:
        if a>c:
            return a
        else:
            return c
    else:
        if b>c:
            return b
        else:
            return c
 
a=input("Enter a")
b=input("Enter b")
c=input("Enter c")
print("Greatest of 3 is :",greatest(a,b,c))
