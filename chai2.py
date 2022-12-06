# n=int(input("enter no:"))
# i=1
# k=ord("A")
# while i<=n:
#     j=1
#     while j<=n:
#         print(chr(k),end=" ")
#         j=j+1
#         k=k+1
#     i=i+1
#     print( )    

n=int(input("enter no:"))
i=1
k=ord("U")
while i<=n:
    j=1
    while j<=n:
        print(chr(k),end=" ")
        j=j+1
        k=k+1
    i=i+1
    k=k-10
    print( )    