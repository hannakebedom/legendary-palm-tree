#Hanna Kebedom, COMP 1405, ASSIGNMENT 5

#load from function
def loadfrom(userinput):
    ''' Loads the student data from the file called 'filename' (located in the same directory) '''
    try:
        words = userinput.split()
        filename = words[2]
        file = open(filename,'r')
        return filename
    except FileNotFoundError:
        print('Sorry, that file cannot be found. Make sure the file is located in the same directory')

#show [number] function
def show(userinput,filename):
    ''' Displays to the screen the first n students in the data. If number, n, is not provided then all students are displayed.  '''
    try:
        #prints all students if number is not provided
        if userinput.lower() == 'show':
            file = open(filename,'r')
            file.seek(0)
            all_contents = file.read()
            print(all_contents)
        #if number, n, is provided, program prints the first n strudents
        else:
            file = open(filename,'r')
            words = userinput.split()
            number = int(words[1])
            file.seek(0)
            if number < 0:
                print("Please enter a positive number, n, after 'show'") #asks user to enter a positive number if they enter a negative one
            elif number <= len(open(filename).readlines()): #if number is smaller than or equal to the number of students in file, program prints specified number 
                for i in range(number):
                    line = file.readline()
                    line = line.strip()
                    print(line, end = '\n')
            else:            #if number is bigger than the number of students in the file, then all students are printed                            
                all_contents = file.read()
                print(all_contents)
        file.close()
    except ValueError:
        print("Enter a positive number, n, after 'show' in the format 'show n' to display the first n students in the data. Enter 'show' to view all students in data")
    except IndexError:
        print("Enter a positive number, n, after 'show' in the format 'show n' to display the first n students in the data. Enter 'show' to view all students in data")
    except NameError:
        print("Please load a file before using this command")
        
# sort by name function
def sortname(filename):
    ''' Sorts the data by the students' names. First by last name and then by first name when the last names are the same. If both first and last names are the same then by ID number '''
    #open file
    file = open(filename,'r')
    lines = file.readlines()
    container = []
    #putting data from file into a list of lists to facilitate processing
    for i in range(len(lines)):
        line = lines[i].split(',')
        for i in range(len(line)):
            line[i] = line[i].strip()
            line[i] = line[i].lower()
        container += [line]
        for i in range(len(line)):
            line[i] = line[i].strip()
        original += [line]
    #print(original)
    #print(container)
    #creating seperate lists for lastnames, firstnames and idnumbers
    lastnames  = []
    firstnames = []
    idnumbers = []
    for i in range(len(container)):
        lastname = container[i][0].strip()
        lastnames += [[lastname]]
        firstname = container[i][1].strip()
        firstnames += [firstname]
        idnumber = container[i][2].strip()
        idnumbers += [idnumber]
    #checking to see if any students have the same last name, if two last names are the same, add first name to differentiate
    for i in lastnames:
        count = lastnames.count(i)
        if count > 1: 
            indexes = []
            for j in range(len(lastnames)):
                if lastnames[j] == i:
                    indexes.append(j)
            for k in indexes:
                lastnames[k] += [firstnames[k]] #add firstname
    #checking to see if any students have the same last name and first name, if two students have the same first and last name, add ID number to differentiate
    for i in lastnames:
        count = lastnames.count(i)
        if count > 1:
            indexes = []
            for j in range(len(lastnames)):
                if lastnames[j] == i:
                    indexes.append(j)
            for k in indexes:
                lastnames[k] += [int(idnumbers[k])] #add id number
    #INSERTION SORT (sort list of lastnames alphabetically using insertion sort)
    for index in range(1,len(lastnames)):
        pos = index
        while pos >= 1 and lastnames[pos-1] > lastnames[pos]:
            tmp = lastnames[pos]
            lastnames[pos] = lastnames[pos-1]
            lastnames[pos-1] = tmp
            pos -= 1 
    string = ''
    
    #write student data (ordered by name) to the file at hand
    file = open(filename,'w')
    file.seek(0)
    for i in range(len(lastnames)):
        for j in range(len(container)):
            if len(lastnames[i]) == 1:
                if lastnames[i][0] in container[j]:
                    if lastnames[i] != lastnames[-1]:
                        string += ', '.join(container[j]) + '\n'
                        break
                    else:
                        string += ', '.join(container[j])
                        break
            elif len(lastnames[i]) == 2:
                if (lastnames[i][0] in container[j]) and (lastnames[i][1] in container[j]):
                    if lastnames[i] != lastnames[-1]:
                        string += ', '.join(container[j]) + '\n'
                        break
                    else:
                        string += ', '.join(container[j])
                        break
                else:
                    continue
            elif len(lastnames[i]) > 2:
                if ((lastnames[i][0] in container[j]) and (lastnames[i][1] in container[j]) and (str(lastnames[i][-1]) in container[j])):
                    if lastnames[i] != lastnames[-1]:
                        string += ', '.join(container[j]) + '\n'
                        break
                    else:
                        string += ', '.join(container[j])
                        break
                else:
                    continue
    file.write(string)
    file.flush()
    file.close()

#sort by grades function
def sortgrade(filename):
    '''Sorts the data by the students' grades in decreasing order (highest grade first)'''
    #open file 
    file = open(filename,'r')
    lines = file.readlines()
    container = []
    #putting data from file into a list of lists to facilitate processing
    for i in range(len(lines)):
        line = lines[i].split(',')
        for i in range(len(line)):
            line[i] = line[i].strip()
        container += [line]
    grades = []
    #create a list of grades from student data
    for i in range(len(container)):
        grade = container[i][3].strip()
        grades += [int(grade)]
    #SELECTION SORT (sorting grades from highest to lowest)
    for index in range(len(grades)):
        minPos = index
        for pos in range(index+1,len(grades)):
            if grades[pos] > grades[minPos]:
                minPos = pos
        tmp = grades[index]
        grades[index] = grades[minPos]
        grades[minPos] = tmp
    #write student data (ordered by grades, highest to lowest) to the file at hand
    string = ''
    done = []
    file = open(filename,'w')
    file.seek(0)
    for i in range(len(grades)):
        for j in range(len(container)):
            if (str(grades[i]) in container[j]) and (container[j] not in done):
                if i != len(grades)-1:
                    string += ', '.join(container[j])+ '\n'
                    break
                else:
                    string += ', '.join(container[j])
                    break
        done += [container[j]]
    file.write(string)
    file.flush()
    file.close()

#find function
def find(userinput,filename):
    '''Finds and displays to the screen all students with a given lastname. Assumes sort by name has already been performed'''
    try: 
        words = userinput.split()  
        name = words[1]          #identify name to be found (from userinput)
        #open file
        file = open(filename,'r')
        lines = file.readlines()
        #organize student data into a list of lists
        container = []
        for i in range(len(lines)):
            line = lines[i].split(',')
            for i in range(len(line)):
                line[i] = line[i].strip()
                line[i] = line[i]
            container += [line]
        lastnames  = []
        #create a list of lastnames from student data
        for i in range(len(container)):
            lastname = container[i][0].strip()
            lastnames += [lastname]
        left = 0 
        right = len(lastnames)-1
        indexlist = []
        #HYBRID BINARY SEARCH (search sorted data for specified name)
        while (left <= right):
            middle = (left + right) // 2  
            if lastnames[middle].lower() == name.lower():
                index = middle
                indexlist += [index]
                break
            elif lastnames[middle].lower() < name.lower():
                left = middle + 1
            else:
                right = middle - 1
        for i in range(0, len(lastnames)):  #check to see if any other students with the same name exist a
            if lastnames[i].lower() == name.lower() and i != index:
                indexlist += [i]
        if len(indexlist) == 0:
            print("No students with the name '" + name + "' found") #return this message if no student was found with specified name
        else:
            for j in range(len(container)):
                for i in container[j]:
                    if name.lower() == i.lower():
                        print(', '.join(container[j]))   #return student data of student with specified name
    except IndexError:
        print("Please enter the name you are searching for after find")

def transcript(userinput,commandnumber):
    '''Adds commands entered by the user to the transcript.txt file'''
    if commandnumber == 1:
        file = open('transcript.txt','w')
        file.write(userinput + '\n')
        file.flush()
        file.close()
    else: 
        file = open('transcript.txt','a')
        file.write(userinput + '\n')
        file.flush()
        file.close()
    
#main function (drives program)
def main():
    print('Welcome to the student data program')
    print('-----------------------------------------')
    #receive command
    userinput = ''
    commandnumber = 0
    while userinput.lower() != 'quit':
        userinput = str(input('command: '))
        commandnumber += 1
        transcript(userinput,commandnumber)
        try:
            if userinput.lower() == 'quit':
                print('Good-bye!')
                continue
            #load from filename
            elif 'load from' in userinput.lower():
                filename = loadfrom(userinput)
            #show [number]
            elif 'show' in userinput.lower():
                show(userinput,filename)
            #sort by name
            elif userinput.lower() == 'sort by name':
                sortname(filename)
            #sort by grades
            elif userinput.lower() == 'sort by grades':
                sortgrade(filename)
            #find name
            elif 'find' in userinput.lower():
                find(userinput, filename)
            #command not recognized
            else:
                print('Sorry, that command is not recognized')
        except UnboundLocalError:
            print("Please load a file before using this command.")

#main guard
if __name__ == '__main__':
    main()