#Hanna Kebedom, COMP 1405
divider = '--------------------------------------------'
print(divider)

print('COMP 1405 Grade Calculator')

print (divider)

studentname = input('Please enter your name: ')

print(divider)

#Receive grades from student
assignmentgrade = float(input(studentname + ', please enter your assignment grade : '))
midterm1grade = float(input(studentname + ', please enter your midterm 1 grade : '))
midterm2grade = float(input(studentname + ', please enter your midterm 2 grade : '))
finalexamgrade = float(input(studentname + ', please enter your final exam grade : '))

print (divider)

#Determine if student did better on midterm 1 or midterm 2 and calculate weighting appropriately
if midterm1grade >= midterm2grade:
    midtermgradecase1 = midterm1grade*0.12 + midterm2grade*0.12 #Weighting of midterms if student performed better on midterm 1
    finalexamgrade = finalexamgrade*0.26
    if midtermgradecase1 + finalexamgrade < 25 :  #Check if student passed combined midterms and final
        finalgrade = 2*(midtermgradecase1 + finalexamgrade)
    else:
        finalgrade = (midtermgradecase1 + assignmentgrade*0.50 + finalexamgrade)
else:
    midtermgradecase2 = midterm1grade*0.08 + midterm2grade*0.16 #Weighting of midterms if student performed better on midterm 2
    finalexamgrade = finalexamgrade*0.26
    if midtermgradecase2 + finalexamgrade < 25:  #Check if student passed combined midterms and final
        finalgrade = 2*(midtermgradecase2 + finalexamgrade)
    else:
        finalgrade = (midtermgradecase2 + assignmentgrade*0.50 + finalexamgrade)

print(studentname + "'s final grade is, " + str(finalgrade))


