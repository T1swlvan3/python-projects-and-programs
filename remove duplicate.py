#Remove all duplicate elements from a list and print the updated list

#using SET
a=[1,1,2,2,3,3,4,5,6,6,7,8,9,9]
b=set(a)
a=list(b)
print("Updated List:",a)
print("-----------------------")

#using for loop
a=[1,1,2,2,3,3,4,5,6,6,7,8,9,9]
b=[ ]
for i in a:
    if i not in b:
        b.append(i)
print("Updated List:",b)
