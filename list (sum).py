#write a python program to find sum of all elements in a list

#Getting values from user and find sum of all elements in a list
mylist=[]
value=int(input("Enter how many values you need to add:"))
for i in range(value):
    a=input("Enter your value:")
    mylist.append(a)
print(mylist)
b=0
for i in mylist:
    c=b+int(i)
    b=c
print("sum of all elemwnts in a list:",c)

print("------------------------------")

#Getting values from user using MAP and Split function and find sum of all elements in a list
mylist=list(map(int,input("enter all values need to be added with space :").split()))
b=0
for i in mylist:
    c=b+int(i)
    b=c
print("sum of all elemwnts in a list:",c)

print("------------------------------")

#Getting values from user using MAP and Split function and find sum of all elements in a list using SUM function
mylist=list(map(int,input("enter all values need to be added with space :").split()))
print("sum of all elemwnts in a list:",sum(mylist))
