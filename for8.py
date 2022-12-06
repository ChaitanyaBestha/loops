n=int(input("enter no:"))
for i in range(n,1,-2):
    print(" "*(n-i)+"* "*i)
for i in range(1,n,2):
    print(" "*(n-i)+"* "*i)