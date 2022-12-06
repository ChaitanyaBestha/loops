n=int(input("enter no:"))
i=0
min=1000
max=0
while i<n:
    user=int(input("enterno:"))
    if user>max:
        max=user
    if user<min:
        min=user
    i=i+1
print(max)
print(min)            