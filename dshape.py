r=5
c=5
i=1
while i<=r:
    j=1
    while j<=c:
        if i==1 or i==5:
            print("*",end=" ")
        elif j==2 or j==5:
            print("*",end=" ")
        else:
            print(" ",end=" ")        
        j=j+1
    i=i+1
    print( )        