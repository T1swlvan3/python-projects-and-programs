#Given a list of integers,find and print the maximum element

#finding using MAX function
mylist=list(map(int,input("enter all values need to be added with space :").split()))
print("The maximum element in the list:",max(mylist))

print("-----------------------------")

#without using MAX function
a=[10,20,90,30,80]
b=0
for i in a:
    if (i>b):
        c=i
        b=i
    else:
        c=b
print("MY List:",a)
print("The maximum element in the list:",c)

    
