# def cal(num_x,num_y,operation):
#     if operation=="+":
#         return num_x+num_y
#     elif operation=="-":
#         return num_x-num_y
#     elif operation=="*":
#         return num_x*num_y
#     elif operation=="/":
#         return  num_x/num_y
# a=int(input("enter the first number:"))
# b=int(input("enter the number:"))
# operator=input("enter the operator:")
# print(cal(a,b,operator))

def cal(l1,l2,multiply):
    if multiply=="*":
        i=0
        b=[]
        while i<len(l1):
            c=l1[i]*l2[i]
            b.append(c)
            i=i+1
        return b
print(cal([10,20,30,40],[50,60,70,80],"*"))

