num=int(input("enter no:"))
f=0
i=1
while i<=num:
    if num%i==0:
        f+=1
    i=i+1
if f==2:
    print("the num is prime")
else:
    print("the num is not prime")        