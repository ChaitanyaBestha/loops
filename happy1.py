n=int(input("enter no:"))
i=n
while i>=10:
    sum=0
    while i>0:
        j=i%10
        sum=sum+j**2
        i=i//10
    i=sum
if i==1:
    print("happy")
else:
    print("not")    
