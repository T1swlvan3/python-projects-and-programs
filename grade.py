def get_grade(mark):
    if mark >= 90:
        return "A+"
    elif mark >= 80:
        return "A"
    elif mark >= 70:
        return "B"
    elif mark >= 60:
        return "C"
    elif mark >= 50:
        return "D"
    else:
        return "F"

subjects = ["Tamil", "English", "Maths", "Science", "Social"]

marks = []

for subject in subjects:
    mark = eval(input("Enter mark for " + subject + ": "))
    marks.append(mark)

print("\n----- RESULT -----")

for i in range(len(subjects)):
    print(subjects[i], "- Mark:", marks[i], "Grade:", get_grade(marks[i]))
