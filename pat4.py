n=int(input("enter no:"))
i=1
while i<=n:
    k=0
    while k<(n-i)-1:
        print(" ",end=" ")
        k=k+1
    j=1
    while j<=i:
        print(j,end=" ")
        j=j+1
    i=i+1
    print( )        