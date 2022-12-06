n=int(input("enter no:"))
# k=ord("A")
for i in range(n):
    k=ord("A")+i
    for j in range(i+1):
        print(chr(k),end=" ")
        k=k+1
    print( )    