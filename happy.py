n=int(input("enter no:"))
temp=n
while sum!=1:
    sum=0
    while temp!=0:
        r=temp%10
        sum=sum+r*r
        temp=temp//10
    temp=sum
if sum==1:
    print("happy number")
else:
    print("not happy")        

