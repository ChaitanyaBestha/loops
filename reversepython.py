n=input("enter word:")
a=len(n)
i=0
while i<a:
    j=i
    while j>=0:
        print(n[j],end=" ")
        j=j-1
    i=i+1
    print()
