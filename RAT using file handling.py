def NRRAT ():
    f=open("RAT.txt","w+")
    f.write("Number Row Right Angle Triangle \n-------------\n")
    for i in range(0,6):
        for j in range (0,i+1):
            f.write(str(i))
        f.write("\n")
    f.close()

def NCRAT ():
    f=open("RAT.txt","a")
    f.write("\n Number Column Right Angle Triangle \n-------------\n")
    for i in range(1,6):
        for j in range (1,i+1):
            f.write(str(j))
        f.write("\n")
    f.close()

def SRRAT ():
    a="tamil"
    f=open("RAT.txt","a")
    f.write("\n String Row Right Angle Triangle \n-------------\n")
    for i in range(0,len(a)):
        for j in range (0,i+1):
            f.write(a[i])
        f.write("\n")
    f.close()

def SCRAT ():
    a="tamil"
    f=open("RAT.txt","a")
    f.write("\n String Column Right Angle Triangle \n-------------\n")
    for i in range(0,len(a)):
        for j in range (0,i+1):
            f.write(a[j])
        f.write("\n")
    f.close()

def symbole():
    f=open("RAT.txt","a")
    f.write("star Right Angle Triangle \n-------------\n")
    for i in range(0,6):
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
        NRRAT()
    elif (n==2):
        NCRAT()
    elif (n==3):
        SRRAT()
    elif (n==4):
        SCRAT()
    elif (n==5):
        symbole()
    else:
        print("invalid choise")
    a=int(input("enter 1 for start , 2 for stop:"))      
       
       

    
      
        
    
