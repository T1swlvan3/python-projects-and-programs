#Given a list of integer, create a new list with only odd number

a=[1,2,3,4,5,6,7,8,9]
b=[]
print("Given list ",a)
for i in a:
    if (i%2 != 0):
        b.append(i)
print("New list with only odd number",b)
