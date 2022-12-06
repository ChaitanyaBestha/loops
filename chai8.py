n=input("enter word")
a=len(n)
i=a
while i>=0:
    j=0
    while j<i:
        print(n[j],end=" ")
        j=j+1
    i=i-1
    print( )    