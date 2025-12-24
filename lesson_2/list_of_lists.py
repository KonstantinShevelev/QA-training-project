#student1 = [100,80,95,84]
#student2 = [68,99,70,95]
# = [40,100,95,80]
#student4 = [65,70,68,80]
#student5 = [70,79,85,96]

grades = [[100,80,95,84],[68,99,70,95],[40,100,95,80],[65,70,68,80],[70,79,85,96]]

for lst in grades:
    print("Student's Grades: ")
    for exam_no in range(len(lst)):
        print("Exam " + str(exam_no + 1) + ": " + str(lst[exam_no]))