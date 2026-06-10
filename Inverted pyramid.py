def num():
    rows=6
    print("Number Column Inverted Pyramid")
    for i in range(rows,0,-1):
        print(" " * (rows - i), end="")
        for j in range(1,i+1):
            print(j, end=" ")
        print()

def numc():
    rows=6
    print("Number Column Inverted Pyramid")
    for i in range(rows,0,-1):
        print(" " * (rows - i), end="")
        for j in range(1, i+1):
            print(i, end=" ")
        print()

def letter():
    rows="tamil"
    print("String Row Inverted Pyramid")
    for i in range(len(rows),0,-1):
        print(" " * (len(rows) - i), end="")
        for j in range(0, i ):
            print(rows[j], end=" ")
        print()

def letterc():
    rows="tamil"
    print("String Column Inverted Pyramid")
    for i in range(len(rows)-1,-1,-1):
        print(" " * (len(rows) - i), end="")
        for j in range(0, i +1):
            print(rows[i], end=" ")
        print()

def star():
    rows=6
    print("Star Pyramid")
    for i in range(rows,0,-1):
        print(" " * (rows - i), end="")
        for j in range(1, i + 1):
            print("*", end=" ")
        print()
num()
numc()
letter()
letterc()
star()
