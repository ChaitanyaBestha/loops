num=int(input("enter no:"))
temp=num
rev=0
while num>0:
     a=num%10
     rev=rev*10+a
     num=num//10
if rev==temp:
      print("palindrome")
else:
      print("not") 
