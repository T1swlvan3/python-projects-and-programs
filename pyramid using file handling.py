def num():
    rows=6
    f=open("Pyramid.txt","w+")
    f.write("Number Row Pyramid \n")
    for i in range(1, rows + 1):
        f.write(" " * (rows - i))
        for j in range(1, i + 1):
            f.write(str(j))
            f.write(" ")
        f.write("\n")

def numc():
    rows=6
    f=open("Pyramid.txt","a")
    f.write("Number Column Pyramid \n")
    for i in range(1, rows + 1):
        f.write(" " * (rows - i))
        for j in range(1, i + 1):
            f.write(str(i))
            f.write(" ")
        f.write("\n")

def letter():
    rows="tamil"
    f=open("Pyramid.txt","a")
    f.write("String Row Pyramid \n")
    for i in range(0, len(rows) + 1):
        f.write(" " * (len(rows) - i))
        for j in range(0, i ):
            f.write(rows[j])
            f.write(" ")
        f.write("\n")

def letterc():
    rows="tamil"
    f=open("Pyramid.txt","a")
    f.write("String Column Pyramid \n")
    for i in range(0, len(rows)):
        f.write(" " * (len(rows) - i))
        for j in range(0, i +1):
            f.write(rows[i])
            f.write(" ")
        f.write("\n")

def star():
    rows=6
    f=open("Pyramid.txt","a")
    f.write("Star Pyramid \n")
    for i in range(1, rows + 1):
        f.write(" " * (rows - i))
        for j in range(1, i + 1):
            f.write("*")
            f.write(" ")
        f.write("\n")
num()
numc()
letter()
letterc()
star()
