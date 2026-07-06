#write a program to check the given string is palindrom or not

#Using For loop
a=input("Enter a word to check palindrom or not:")
b=""
for i in range(len(a)-1,-1,-1):
    b=b+(a[i])
if(a==b):
    print(a," is palindrom")
else:
    print(a," is not palindrom")
print("---------------------")

#without using For loop
a=input("Enter a word to check palindrom or not:")
b=a[::-1]
if(a==b):
    print(a," is palindrom")
else:
    print(a," is not palindrom")
print("---------------------------")

#Using Reversed function
a=input("Enter a word to check palindrom or not:")
b="".join(reversed(a))
if(a==b):
    print(a," is palindrom")
else:
    print(a," is not palindrom")
