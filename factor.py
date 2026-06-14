def factor():
    num=int(input("enter a two digit number:"))
    print ("Factors of ",num)
    for i in range (1,num+1):
        if (num%i==0):
            print(i,end=" ")
factor()
