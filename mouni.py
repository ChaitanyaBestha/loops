
i=65
while i<=69:
    k=1
    while k<=69-i:
        print(" ",end=" ")
        k=k+1
    j=i
    while j>=65:
        print(chr(j),end=" ")
        j=j-1
        k=k+1
    m=66
    while m<=i:
        print(chr(m),end=" ")
        m=m+1    
    i=i+1
    print()    
