def NRIRAT ():
    f=open("IRAT.txt","w+")
    f.write("Number Row Inverted Right Angle Triangle \n-------------\n")
    for i in range(6,0,-1):
        for j in range (0,i):
            f.write(str(i))
        f.write("\n")
    f.close()

def NCIRAT ():
    f=open("IRAT.txt","a")
    f.write("\n Number Column Inverted Right Angle Triangle \n-------------\n")
    for i in range(6,0,-1):
        for j in range (0,i):
            f.write(str(j))
        f.write("\n")
    f.close()

def SRIRAT ():
    a="tamil"
    f=open("IRAT.txt","a")
    f.write("\n String Row Inverted Right Angle Triangle \n-------------\n")
    for i in range(len(a)-1,-1,-1):
        for j in range (0,i+1):
            f.write(a[i])
        f.write("\n")
    f.close()

def SCIRAT ():
    a="tamil"
    f=open("IRAT.txt","a")
    f.write("\n String Column Inverted Right Angle Triangle \n-------------\n")
    for i in range(len(a)-1,-1,-1):
        for j in range (0,i+1):
            f.write(a[j])
        f.write("\n")
    f.close()

def SIRAT():
    f=open("IRAT.txt","a")
    f.write("star Inverted Right Angle Triangle \n-------------\n")
    for i in range(6,0,-1):
        f.write("*"*i)
        f.write("\n")
    f.close()

a=int(input("enter 1 for start , 2 for stop:"))
while (a==1):
    print ('''choose what to print
            1.Number Row Right Angle Triangle 
            2.Number Column Right Angle Triangle
            3.String Row Right Angle Triangle
            4.String Column Right Angle Triangle
            5.star Right Angle Triangle
            6.sybmole inverted right angle triangle''')
    n=int(input("enter your choise"))
    if (n==1):
        NRIRAT()
    elif (n==2):
        NCIRAT()
    elif (n==3):
        SRIRAT()
    elif (n==4):
        SCIRAT()
    elif (n==5):
        SIRAT()
    else:
        print("invalid choise")
    a=int(input("enter 1 for start , 2 for stop:"))      
       
       

    
      
        
    
