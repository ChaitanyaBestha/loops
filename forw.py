n=int(input("enter no:"))
for i in range(n):
    k=ord("A")
    for j in range(i+1):
        print(chr(k),end=" ")
        k=k+1
    print( )    