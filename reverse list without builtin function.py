#reverse a list without using any builtin function

#without using for loop
a=[1,2,3,4,5,6]
b=a[::-1]
c=[]
print("Given List:",a)
print("Reverse list:",b)
print("\n ------------------------- \n")


#with for loop
a=[1,2,3,4,5,6]
b=[]
for i in range(len(a)-1,-1,-1):
    b.append(a[i])
print("Given List:",a)
print("Reverse list:",b)
    
