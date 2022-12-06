r=5
c=3
i=1
while i<=r:
    j=1
    while j<=c:
        if i==5 or i==1 or j==2:
            print("*",end=" ")
        else:
            print(" ",end=" ")        
        j=j+1
    i=i+1
    print( )       