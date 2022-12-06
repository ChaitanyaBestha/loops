n=int(input("enter no:"))
i=1
k=ord("A")
while i<=n:
    j=1
    while j<=i:
        if i%2!=0:
            print(chr(k),end=" ")
        if i%2==0:
            print(i,end=" ")
        j=j+1
    k=k+1
    i=i+1
    print()            