n=int(input("enter the no:"))
i=1
v=1
while i<=n:
    j=1
    while j<=n:
        if i==1:
            print(v,end="  ")
        elif i==2 and j!=4:
            print(v+7,end=" ")
        elif (i==2 and j==4) or (i==4 and j==1):
            print(v-3,end=" ")
        elif (i==3 and j==1):
            print(v+2,end=" ")
        elif (i==3 and j==2):
            print(v+6,end=" ")
        elif(i==3 and j==3):
            print(v+4,end=" ")
        elif(i==3 and j==4):
            print(v-6,end=" ")                                                                                                 
        elif(i==4 and j==2):
            print(v-5,end="  ")
        elif(i==4 and j==3):
            print(v-7,end="  ")
        elif(i==4 and j==4):
            print(v-9,end="  ")
        j=j+1
        v=v+1
    i=i+1
    print()