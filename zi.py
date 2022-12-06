n=int(input("enter no"))
i=1
while i<=n:
    k=1
    while k<=n-i:
        print(" ",end="")
        k=k+1
    j=1
    while j<=i:
        print("*",end=" ")
        j=j+1 
    i=i+2
    print( )  
i=n-2
while i>=1:
    k=0
    while k<=n-i:
        print(" ",end="")  
        k=k+1
    j=0
    while j<i:
        print("*",end=" ")
        j=j+2
    i=i-2
    print( )    