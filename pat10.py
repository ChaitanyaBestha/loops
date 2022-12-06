n=int(input("enter rows"))
i=1
while i<=n:
    k=1
    while k<=n-i:
        print(" ",end=" ")
        k=k+1
    j=1
    while j<=i:
        print(i,end=" ")
        j=j+1
    m=2
    while m<=i:
        print(i,end=" ")
        m=m+1
    i=i+1
    print( )            