n=input("enter word")
a=len(n)
i=a
while i>=0:
    k=0
    while k<=(a-i):
        print(" ",end=" ")
        k=k+1
    j=0
    while j<i:
        print(n[j],end=" ")
        j=j+1
    i=i-1
    print( )        