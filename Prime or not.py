#determine the given number is prime or not

a=int(input("Enter a number to determine prime or not :"))
count=0
for i in range(1,a):
    if (a%i==0):
        count=count+1
if(a<=1):
    print(a,"is Neither Prime nor Composite")
elif(count==1):
    print(a,"is Prime number")
else:
    print(a,"is Not a Prime number")
