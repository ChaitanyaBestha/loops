# n=int(input("enter no:"))
# i=1
# k=ord("a")
# while i<=n:
#     j=1
#     while j<=i:
#         print(chr(j),end=" ")
#         j=j+1
#     i=i+1
#     print( )    


user=int(input("enter the number"))
i=1
even=0
sum=0
while i<=user:
    # user=int(input("enter the number"))
    if i%2==0:
        even=even+1
    i=i+1
    print("even")