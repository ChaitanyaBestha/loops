def reverse_string(str):
    str1=""
    for i in str:
        str1=i+str1
    return str1
str="chaitanya"
print("the original string is",str)
print("the reverse ",reverse_string(str))