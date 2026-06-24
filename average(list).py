#Calculate the average of all numbers in a list

#find Average of all elements in a list
mylist=[1,2,5,4,69,8,7,5,2,16,5]
b=0
for i in mylist:
    c=b+int(i)
    b=c
average=c/len(mylist)
print("Average of all elemwnts in a list:",average)

print("------------------------------")

#Find Average of all elements in a list using SUM function
mylist=[1,2,5,4,69,8,7,5,2,16,5]
average = sum(mylist)/len(mylist)
print("Average of all elemwnts in a list:",average)

