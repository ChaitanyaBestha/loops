n=int(input("enter no:"))
i=1
while i<=n:
    j=5
    k=ord("A")
    while j>=i:
        print(chr(k),end=" ")
        k=k+1
        j=j-1   
    i=i+1
    print( )  