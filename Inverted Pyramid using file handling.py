def num():
    rows=6
    f=open("Inverted Pyramid.txt","w+")
    f.write("Number Row Inverted Pyramid  \n")
    for i in range(rows,0,-1):
        f.write(" " * (rows - i))
        f.write(" ")
        for j in range(1,i+1):
            f.write(str(j))
            f.write(" ")
        f.write("\n")

def numc():
    rows=6
    f=open("Inverted Pyramid.txt","a")
    f.write("Number Column Inverted Pyramid  \n")
    for i in range(rows,0,-1):
        f.write(" " * (rows - i))
        f.write(" ")
        for j in range(1, i+1):
            f.write(str(i))
            f.write(" ")
        f.write("\n")

def letter():
    rows="tamil"
    f=open("Inverted Pyramid.txt","a")
    f.write("String Row Inverted Pyramid  \n")
    for i in range(len(rows),0,-1):
        f.write(" " * (len(rows) - i))
        f.write(" ")
        for j in range(0, i ):
            f.write(rows[j])
            f.write(" ")
        f.write("\n")

def letterc():
    rows="tamil"
    f=open("Inverted Pyramid.txt","a")
    f.write("String Column Inverted Pyramid  \n")
    for i in range(len(rows)-1,-1,-1):
        f.write(" " * (len(rows) - i))
        f.write(" ")
        for j in range(0, i +1):
            f.write(rows[i])
            f.write(" ")
        f.write("\n")

def star():
    rows=6
    f=open("Inverted Pyramid.txt","a")
    f.write("Star Inverted Pyramid  \n")
    for i in range(rows,0,-1):
        f.write(" " * (rows - i))
        f.write(" ")
        for j in range(1, i + 1):
            f.write("*")
            f.write(" ")
        f.write("\n")
num()
numc()
letter()
letterc()
star()
