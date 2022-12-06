n=int(input("enter no:"))
i=1
k=ord("U")
while i<=n:
    j=1
    # k=ord("Y")
    while j<=n:
        if i==1:
            print(chr(k),end=" ")
        elif i==2:
            print(chr(k),end=" ")
        elif i==3:
            print(chr(k),end=" ")
        elif i==4:
            print(chr(k),end=" ")
        elif i==5:
            print(chr(k),end=" ")
        else:
            print("nothing") 
        k=k+1           
        j=j+1
    i=i+1
    k=k-10
    print( )     