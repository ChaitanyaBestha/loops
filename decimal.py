n=int(input("enter no:"))
k=0
i=0
len=len(str(n))
while i<=len: 
    r=n%10
    k=k+r*2**i
    n=n//10
    i=i+1
print(k)    

# n=int(input("enter no:"))
# i=0
# while n>0:
#     r=n%2
#     n=n//2
#     i=i+1
#     print(r,end=" ")
# k=0
# while i>0:
#     m=i%10
#     k=k*10+m
#     i=i//10
# print(k)    

# n=int(input("enter the number:"))
# k=0
# while n>0:
#     r=n%2
#     n=n//2
#     k=k*10+r
# print(k)
# i=0
# while k>0:
#     m=k%10
#     i=i*10+m
#     k=k//10
# print(i)

