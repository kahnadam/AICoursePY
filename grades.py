names = list(input("Please enter names separated by commas: ").split(","))
assignments = list(input("Please enter assignments separated by commas: ").split(","))
grades = list(input("Please enter grades separated by commas: ").split(","))

message = "Hi {},\n\nThis is a reminder that you have {} assignments left to \
submit before you can graduate. You're current grade is {} and can increase \
to {} if you submit all assignments before the due date.\n\n"

def max_grade(gr,assig):
    gr = int(gr)
    assig = int(assig)
    return str(gr + assig * 2)

for i in range(0,len(names)):
    print(message.format(names[i].title(),
    assignments[i],
    grades[i],
    max_grade(grades[i],assignments[i])
    ))
