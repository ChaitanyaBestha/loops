n=int(input("enter no:"))
temp=n
i=1
sum=0
while i<n:
    if n%i==0:
        sum=sum+i
    i=i+1 
print(sum)   
if sum==temp:
    print("it is a perfect number")
else:
    print("it is not perfect number")    
