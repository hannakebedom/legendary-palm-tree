#Hanna Kebedom, COMP 1405
def grade2letter(grade):
    if grade >= 0 and grade < 50:
        return 'F'
    elif grade >= 50 and grade < 60:
        return 'D'
    elif grade >= 60 and grade < 70:
        return 'C'
    elif grade >= 70 and grade < 80:
        return 'B'
    elif grade >= 80 and grade < 90:
        return 'A'
    elif grade >= 90 and grade <= 100:
        return 'A+'
    else:
        return 'Invalid input. Enter a number from 0-100'

def testgrade2letter():
    divider = "---------------------------------------"
    print(divider)
    print('Test Cases:')
    for i in [[49.9,'F'], [50,'D'], [59.9,'D'], [60,'C'],[69.9,'C'],[70,'B'],[79.9,'B'], [80,'A'], [89.9,'A'], [90,'A+'],[99.9,'A+'],[100,'A+']]:
        inputvalue = i[0]
        expectedoutput = i[1]
        actualoutput = grade2letter(inputvalue)
        print(divider)
        print ('Input Value:' + str(inputvalue))
        print ('Expected Output: ' + str(expectedoutput))
        print ('Actual Output: ' + str(actualoutput))
        testequal(actualoutput, expectedoutput)

def testequal(x,y):
    if x==y:
        print('Pass')
    else:
        print('Fail')