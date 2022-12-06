# n=int(input("enter no:"))
# for i in range(n):
#     for j in range(i+1):
#         print(i+1,end=" ")
#     print( )    

# n=int(input("enter no:"))
# i=1
# k=ord("A")
# while i<=n:
#     j=1
#     # k=ord("A")
#     while j<=i:
#         print(chr(k),end=" ")
#         # k=k+1
#         j=j+1
#     k=k+1    
#     i=i+1
#     print( )    

# n=int(input("enter no"))
# k=ord("U")
# for i in range(n):
#     # k=ord("Y")
#     for j in range(1,n,1):
#         print(chr(k),end=" ")
#         # k=k-1
#         k=k-1
#     print( )  

n=int(input("enter no:"))
for i in range(n):
    for j in range(i+1):
        print(i+1,end=" ")
    for j in range(2,n,-1):
        print(j,end=" ")
    print()        