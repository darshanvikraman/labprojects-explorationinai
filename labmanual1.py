name = input("enter student name")
n = int(input("enter number of subjects: "))
total = 0
for i in range(1, n+1):
    mark = float(input(f"enter mark for subject {i} : "))
    total += mark
    percentage = total/n
    if percentage >= 90:
        grade = "A+"
        performance = "outstanding"
        print(grade,performance)
    elif percentage >= 80:
        grade = "A"
        performance = "excellent"
        print(grade,performance)
    elif percentage >= 70:
        grade = "B"
        performance = "very good"
        print(grade,performance)
    elif percentage >= 60:
        grade = "C"
        performance = "average"
        print(grade,performance)
    elif percentage >= 50:
        grade = "D"
        performance = "bad"
    else:
        grade = "F" 
        performance = "very bad"    