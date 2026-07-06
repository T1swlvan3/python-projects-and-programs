#Reverse a string without using built in function

#Using For loop
a=input("Enter a to be reversed:")
b=""
for i in range(len(a)-1,-1,-1):
    b=b+(a[i])
print("Reversed string:",b)
print("---------------------")

#without using For loop
a=input("Enter a to be reversed:")
b=a[::-1]
print("Reversed string:",b)
