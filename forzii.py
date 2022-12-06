# n=int(input("enter no:"))
# for i in range(n):
#     for j in range(n-i-1):
#         print(" ",end=" ")
#     for j in range(i+1):
#         print(j+1,end=" ") 
#     for j in range(i,-1,-1):
#         print(j+1,end=" ")   
#     print( ) 

n=int(input("enter no:"))
for i in range(1,n,1):
    print(((10**i-1)//9)**2)