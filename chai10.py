n=int(input("enter no:"))
i=1
while i<=n:
    k=0
    while k<=(n-i)-1:
        print(" ",end=" ")
        k=k+1
    j=i
    while j>=1:
        print(i,end=" ")
        j=j-1
    m=2
    while m<=i:
        print(i,end=" ")
        m=m+1    
    i=i+1
    print( )        