# process.py
# --------------
# COMP1005/1405 
# Summer 2020


# make sure the data.csv file is saved in the same directory as this file
# if you are using VS Code, you must change the settings so that it can find 
# the file when it tries to open it.
# Go to Preferences -> Settings
#       Once in Settings,use the search bar to search for InFileDir
#       Check the box for  "Python -> Terminal : Execute In File Dir"
#  

def findByDomain(domain, data):
    name = ''
    listoutput = []
    count0 = data[0].count(domain)
    count1 = data[1].count(domain)
    namecount = ':' + str(count0 + count1)
    if (count0 and count1) > 0:
        for i in range(len(data[0])):
            if ',' == data[0][i]:
                break
            name =  name + data[0][i] 
        namecount = name + namecount
        for i in range (len(data[1])):
            if ',' == data[1][i]:
                break
            name = name + ',' + namecount
        namecount = name + namecount
        listoutput.append(namecount)
        return listoutput
    elif count0 > 0:
        for i in range(len(data[0])):
            if ',' == data[0][i]:
                break
            name =  name + data[0][i] 
        namecount = name + namecount
        listoutput.append(namecount)
        return listoutput
    elif count1 > 0:
        for i in range (len(data[1])):
            if ',' == data[1][i]:
                break
            name = name + data[1][i]
        namecount = name + namecount 
        listoutput.append(namecount)
        return listoutput
    else: 
        return listoutput

def aveNumberOfEmails(lower, upper, data):
    out = []
    email0 = 0
    email1 = 0 
    if (lower < upper) and (1 <= lower) and (upper <= 101):
        out.append(float(lower))
        for i in range(lower,upper+1):
            email0 = 0
            email1 = 0
            age = i
            age = str(age)
            if age in data:
                for i in range(len(data)):
                    if '@' == data[i]:
                        email0 = email0 + 1
            if (age not in data) and (age in data[0]):
                for i in range(len(data[0])):
                    if '@' == data[0][i]:
                        email0 = email0 + 1
            if (age not in data) and (age in data[1]):
                for i in range(len(data[1])):
                    if '@' == data[0][i]:
                        email1 = email1 + 1
            if (email0 and email1) > 0:
                out.append(float(email0+email1))
            elif email0 >= 0:
                out.append(float(email0))
            elif email1 >= 0:
                out.append(float(email1))
    return out


# This function controls the program
def main():
    fname = 'data.csv'           # filename
    
    print("...opening file " + fname + " for reading")
    file = open(fname, 'r')      # open the file for reading

    print("...readong contents of file")
    data = file.readlines()      # read entire contents of file into list of strings
                                 # each line in the file is one string
    print(data)

    print("...closing file " + fname)
    file.close()                 # close the file now that we are done with it

    print("...data is...")
    for line in data:
        print(line, end='')

    # test your findByDomain() and aveNumberOfEmails() functions
    users = findByDomain('carleton.ca', data)
    print(users)

    stats = aveNumberOfEmails(10,20,data)
    print(stats)

    test = aveNumberOfEmails(11,15,"cat,12,no meta, c@carleton.ca, c@cmail.carleton.ca, c@yahoo.ca")
    print(test)

# This if statement is needed so that when you "run" this program it will 
# automatically call the main function.
# If you load this function as a module it will not call main()
if __name__ == "__main__":
    main()