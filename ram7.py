n=int(input("enter no:"))
i=1
while i<=n:
    j=1
    k=5
    while j<=n:
        if i==2:
            print(k-1,end=" ")
        elif i==3:
            print(k-2,end=" ")
        elif i==4:
            print(k-3,end=" ")
        elif i==5:
            print(k-4,end=" ")
        else:
            print(k,end=" ")
        k=k+5
        j=j+1
    i=i+1
    print( )