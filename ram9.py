r=6
c=6
i=1
while i<=r:
    j=1
    while j<=c:
        if j==1 or(i==2 and j==2)or(i==3 and j==3)or(i==4 and j==4)or(i==5 and j==5)or(i==6 and j==6):
            print("1",end=" ")
        elif (i==3 and j==2):
            print("2",end=" ")
        elif (i==4 and j==2)or(i==4 and j==3):
            print("3",end=" ")
        elif (i==5 and j==2)or(i==5 and j==4): 
            print("4",end=" ")
        elif (i==6 and j==2)or(i==6 and j==5):
            print("5",end=" ")
        elif (i==6 and j==3)or(i==6 and j==4):
            print("10",end=" ")
        elif (i==5 and j==3):
            print("6",end=" ")    
        else:
            print(" ",end=" ")
        j=j+1
    i=i+1
    print( )                                