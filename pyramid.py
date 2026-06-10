def num():
    rows=6
    print("Number Column Pyramid")
    for i in range(1, rows + 1):
        print(" " * (rows - i), end="")
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

def numc():
    rows=6
    print("Number Column Pyramid")
    for i in range(1, rows + 1):
        print(" " * (rows - i), end="")
        for j in range(1, i + 1):
            print(i, end=" ")
        print()

def letter():
    rows="tamil"
    print("String Row Pyramid")
    for i in range(0, len(rows) + 1):
        print(" " * (len(rows) - i), end="")
        for j in range(0, i ):
            print(rows[j], end=" ")
        print()

def letterc():
    rows="tamil"
    print("String Column Pyramid")
    for i in range(0, len(rows)):
        print(" " * (len(rows) - i), end="")
        for j in range(0, i +1):
            print(rows[i], end=" ")
        print()

def star():
    rows=6
    print("Star Pyramid")
    for i in range(1, rows + 1):
        print(" " * (rows - i), end="")
        for j in range(1, i + 1):
            print("*", end=" ")
        print()
num()
numc()
letter()
letterc()
star()
