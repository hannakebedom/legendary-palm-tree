# COMP 1005/1405
# Summer 2020

# Assignment 3



#------------------------------------------------------------------#
# provided function - do NOT remove or change
def load_puzzle(filename):
    ''' Reads a sudoku puzzle from the text file filename. 
        Returns a list of lists of integers.  
    '''
    puzzle = [] 
    f = open(filename, "r")
    for line in f:
        puzzle.append( [int(val) for val in line.split(",")] )
    f.close()
    return puzzle




#------------------------------------------------------------------#
#------------------------------------------------------------------#


# your functions go here!

def puzzle_to_string(puzzle):
    row = ''
    p1 = ''
    for i in range(len(puzzle)):
        if i % 3 == 0 and i != 0:
            p1 += '------+-------+------\n'
        row = ''
        for k in range(len(puzzle[i])):
            if puzzle[i][k] == 0:
                puzzle[i][k] = ' '
            if k % 3 == 0 and k != 0:
                row += '| '
            if k == 8:
                row += str(puzzle[i][k])
            else: 
                row += str(puzzle[i][k]) + ' '
        if i == 8:
            p1 += row 
            p1 = str(p1)
        else:
            row += '\n'
            p1 += row
    return p1

def check_rows(puzzle):
    row = []
    for i in range (len(puzzle)):
        for k in range(1,10):
            count = puzzle[i].count(k)
            if count > 1:
                row.append(i)
                break
    return row


def check_columns(puzzle):
    columns = []
    columnone = []
    columntwo = []
    columnthree = []
    columnfour = []
    columnfive = []
    columnsix = []
    columnseven = []
    columneight = [] 
    columnnine = []
    for k in range(0,10):
        for i in range(len(puzzle)):
            if k == 0:
                columnone.append(puzzle[i][k])
            elif k == 1:
                columntwo.append(puzzle[i][k])
            elif k == 2:
                columnthree.append(puzzle[i][k])
            elif k == 3:
                columnfour.append(puzzle[i][k])
            elif k == 4:
                columnfive.append(puzzle[i][k])
            elif k == 5:
                columnsix.append(puzzle[i][k])
            elif k == 6:
                columnseven.append(puzzle[i][k])
            elif k == 7:
                columneight.append(puzzle[i][k])
            elif k == 8:
                columnnine.append(puzzle[i][k])
    columns += [columnone] + [columntwo] + [columnthree] + [columnfour] + [columnfive] + [columnsix] + [columnseven] + [columneight] + [columnnine]
    column = []
    for i in range(len(columns)):
        for k in range(1,10):
            count = columns[i].count(k)
            if count > 1:
                column.append(i)
                break
    return column

def check_subgrids(puzzle):
    subgridrows = []
    subgrids = []
    subgridone = []
    subgridtwo = []
    subgridthree = []
    subgridfour = []
    subgridfive = []
    subgridsix = []
    subgridseven = []
    subgrideight = []
    subgridnine = []
    counter = 0
    for i in range(len(puzzle)):
        for k in range(len(puzzle[i])):
            counter += 1
            if counter % 3 == 0:
                list = []
                list.append(puzzle[i][k-2])
                list.append(puzzle[i][k-1])
                list.append(puzzle[i][k])
                subgridrows += [list]
    for i in range(0, 9, 3 ):
        subgridone.append(subgridrows[i])
    subgrids.append(subgridone)
    for i in range (1 ,9 ,3):
        subgridtwo.append(subgridrows[i])
    subgrids.append(subgridtwo)
    for i in range (2 , 9, 3):
        subgridthree.append(subgridrows[i])
    subgrids.append(subgridthree)
    for i in range (9, 18, 3):
        subgridfour.append(subgridrows[i])
    subgrids.append(subgridfour)
    for i in range (10, 18, 3):
        subgridfive.append(subgridrows[i])
    subgrids.append(subgridfive)
    for i in range (11, 18, 3):
        subgridsix.append(subgridrows[i])
    subgrids.append(subgridsix)
    for i in range (18, 26, 3):
        subgridseven.append(subgridrows[i])
    subgrids.append(subgridseven)
    for i in range (19, 26, 3):
        subgrideight.append(subgridrows[i])
    subgrids.append(subgrideight)
    for i in range (20,len(subgridrows), 3):
        subgridnine.append(subgridrows[i])
    subgrids.append(subgridnine)

    for i in range(len(subgrids)):
        subgrids[i] = subgrids[i][0] + subgrids[i][1] + subgrids[i][2]
   
    subgrid = []
    for i in range(len(subgrids)):
        for k in range(1,10):
            count = 0 
            count = subgrids[i].count(k)
            if count > 1:
                subgrid.append(i)
                break
    return subgrid

#------------------------------------------------------------------#
#------------------------------------------------------------------#



#------------------------------------------------------------------#
# Your "program" is driven by the main method
# Modify as needed
def main():
    filename = str(input('Please enter your sudoku puzzle file: '))
    puzzle = load_puzzle(filename)
    print(puzzle_to_string(puzzle))
    type(puzzle_to_string(puzzle))
    print('Checking puzzle')
    if check_rows(puzzle) == []:
        print('. . . Rows OK' )
    else:
        print('. . . Rows '+ str(check_rows(puzzle)) + ' failed')
    
    if check_columns(puzzle) == []:
        print('. . . Columns OK')
    else:
        print ('. . . Columns ' + str(check_columns(puzzle)) + ' failed')
    
    if check_subgrids(puzzle) == []:
        print('. . . Subgrids OK')
    else:
        print ('. . . Subgrids ' + str(check_subgrids(puzzle)) + ' failed')
#complete or incomplete puzzle
    for i in range(len(puzzle)):
        count = puzzle[i].count(' ')
        if count > 0:
            puzzlestatus = 'Partial '
            break
        else:
            puzzlestatus = 'Complete '

    if (check_rows(puzzle) == []) and (check_columns(puzzle) == []) and (check_subgrids(puzzle) == []):
        print (puzzlestatus + 'Puzzle solution is correct!')
    else:
        print (puzzlestatus + 'Puzzle solution is NOT correct!')

#------------------------------------------------------------------#
# Guard for main function - do NOT remove or change
if __name__ == "__main__":
    main()