n=int(input("enter no:"))
i=1
k=1
while i<=n:
    j=1
    while j<=i:
        print(k+1-j,end=" ")
        j=j+1 
    i=i+1
    k=k+i
    print( )    