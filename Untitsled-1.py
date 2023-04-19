def greatest(a,b,c):
    l=[]
    l=[a,b,c]
    l.sort()
    print(l[-1])

def g2(a,b,c):
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
        
print(g2(1141,-1,100))
            

greatest(1,33,-1)