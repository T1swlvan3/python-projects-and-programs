#Count the number of vowels in a given string

a="tamil"
vowels=["A","E","I","O","U","a","e","i","o","u"]
count=0
for i in a:
    if i in vowels:
        count=count+1
print("Number of vowels in the given string:",count)
