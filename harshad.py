n=int(input("enter no"))
i=n
sum=0
while i>0:
    j=i%10
    sum=sum+j
    i=i//10
if i%sum==0:
    print("harshad")
else:
    print("no")        