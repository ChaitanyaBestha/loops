n=int(input("enter no:"))
i=1
k=ord("A")
while i<=n:
    j=1
    while j<=i:
        print(chr(k),end=" ")
        j=j+1
    k=k+1    
    i=i+1
    print( )    
