# punctuation starter


#get_punctuation function
def get_punctuation(text,punctuation_marks):
    punctuationlist = []
    for i in punctuation_marks:
        punctuationlist += i
    string = ''
    for i in text:
        if i in punctuationlist:
            string += i
    return string

#analyze_punctuation function
def analyze_punctuation(ptext,punctuation_marks):
    punctuationdictionary = {}
    for i in punctuation_marks:
        punctuationdictionary[i] = 0
    for i in punctuation_marks:
        for j in ptext:
            if i == j:
                punctuationdictionary[i] += 1 
    punctuationcount= []
    for i in punctuationdictionary.items():
        punctuationcount += [list(i)]
    return punctuationcount

#display_punctuation_stats function
def display_punctuation_stats(punctuation_stats):
    total = 0
    max = 0
    for i in range(len(punctuation_stats)):
        if punctuation_stats[i][1] > max:
            max = punctuation_stats[i][1]
            index = punctuation_stats[i][0]
    key = max
    punctuation_stats = {element[0]:int(element[1]) for element in punctuation_stats}
    for i in punctuation_stats:
        total += int(punctuation_stats[i])
    string = 'Punctuation Stats ('+ str(total) + ' in total)' + '\n'
    string += '-+----------------------------------------'+ str(key) + '\n' 
    if key != 0:
        onevalue = round(40 / key) 
        for i in punctuation_stats:
            if i == index:
                string += index + '|' + ('#' * 40) + '\n'
                continue
            string += i + '|' + ('#' * (int(punctuation_stats[i]) * int(onevalue))) + '\n'
    string += '-+----------------------------------------'
    return string

#count_ellipses function
def count_ellipses(text):
    ellipses = 0
    count = 0
    for i in text:
        if i == '.':
            count += 1
        if i == ' ':
            continue
        if count >= 3:
            count = 0
            ellipses += 1
        if i in 'abcdefghijklmnopqrstuvwxyzABDCEFGHIJKLMNOPQRSTUVWXYZ':
            count = 0 
            continue 
        if i in '123456789':
            count = 0
            continue
        if i in '''?!,;:'-[]}{()"*/''':
            count = 0 
            continue
    return ellipses


def passorfail(x,y):
    if x == y:
        return 'pass'
    else:
        return 'fail'

def main():
    divider = '-----------------------------------------------------------------------------'
    print(divider)
    print('testing functions')
    print(divider)
    print('testing get_punctuation(text,punctuation_marks) function:')
    print(divider)
    print('1) extracts single punctuation mark from text')
    print("input: ('The quick brown fox jumps over the lazy dog.','.')")
    expectedoutput = '.'
    actualoutput = get_punctuation('The quick brown fox jumps over the lazy dog.','.')
    print('expected output:', expectedoutput)
    print('actual output:', actualoutput)
    print('pass/fail:', passorfail(expectedoutput,actualoutput))
    print(' ')
    print('2) extracts multiple punctuation marks from text ')
    print("input: ('That's my dog's toy! What are you doing?? Please stop.','?'!.')")
    expectedoutput = "''!??."
    actualoutput = get_punctuation("That's my dog's toy! What are you doing?? Please stop.","?'!.'")
    print('expected output:', expectedoutput)
    print('actual output:', actualoutput)
    print('pass/fail:', passorfail(expectedoutput,actualoutput))
    print(' ')
    print('3) returns a string')
    print("input: ('That's my dog's toy! What are you doing?? Please stop.','?'!.')")
    expectedoutput = "<class 'str'>"
    actualoutput = type(get_punctuation("That's my dog's toy! What are you doing?? Please stop.","?'!.'"))
    print('expected output:', expectedoutput)
    print('actual output:', actualoutput)
    print('pass/fail:', passorfail(type(expectedoutput),actualoutput))
    print(divider)
    print('testing analyze_punctuation(ptext, punctuation_marks) function:')
    print(divider)
    print('1) returns a list of lists (inner lists must have length 2 and are ints)')
    print('2) order of inner lists corresponds to input order')
    print('3) computes frequencies of punctuation marks')
    print('4) includes punctuation marks')
    print('''input: ("....!!!'',,.",".!',?")''')
    expectedoutput =[[".",5],["!",3],["'",2],[",",2],['?',0]]
    actualoutput = analyze_punctuation("....!!!'',,.",".!',?")
    print('expected output:', expectedoutput)
    print('actual output:', actualoutput)
    print('pass/fail:', passorfail(expectedoutput,actualoutput)) 
    print(divider)
    print('testing display_punctuation_stats(punctuation_stats) function')
    print(divider)
    print('1) returns a string')
    print('2) shows total count on top line and max value on second line')
    print('3) shows bar plots for each punctuation mark with correct bar lengths')
    print('4) shows bar plots for each punctuation mark in correct order')
    print('5) overall look of output is correct')
    print('''input: ([["!", 3],[".",4],["?",12],["*", 8])''')
    expectedoutput = '''Punctuation Stats (27 in total)
-+----------------------------------------12
!|#########
.|############
?|########################################
*|########################
-+----------------------------------------'''
    actualoutput = display_punctuation_stats([["!", 3], [".", 4], ["?", 12], ["*", 8]])
    print('expected output:', expectedoutput)
    print('actual output:', actualoutput)
    print('pass/fail:', passorfail(expectedoutput,actualoutput))
    print('''input: ([[":", 40],[".",20],["?",2],["*", 8])''')
    actualoutput = display_punctuation_stats([[":", 40],[".",20],["?",2],["*", 8]])
    expectedoutput = '''Punctuation Stats (70 in total)
-+----------------------------------------40
:|########################################
.|####################
?|##
*|########
-+----------------------------------------'''
    print('expected output:', expectedoutput)
    print('actual output:', actualoutput)
    print('pass/fail:', passorfail(expectedoutput,actualoutput))
    print(divider)
    print('testing count_ellipses( text ) function')
    print(divider)
    print('''1) correctly counts ellipses in the middle of a sentence''')
    print('''input: ('This is . . . SO . . . weird.')''')
    expectedoutput = 2
    actualoutput = count_ellipses('This is . . . SO . . . weird.')
    print('expected output:', expectedoutput)
    print('actual output:', actualoutput)
    print('pass/fail:', passorfail(expectedoutput,actualoutput))
    print(' ')
    print('''2) correctly counts ellipses at the end of sentences''')
    print('''input: ('This is SO weird. . . .')''')
    expectedoutput = 1
    actualoutput = count_ellipses('This is SO weird. . . .')
    print('expected output:', expectedoutput)
    print('actual output:', actualoutput)
    print('pass/fail:', passorfail(expectedoutput,actualoutput))
    print(' ')
    print('''3) ignores extra whitespace correctly''')
    print('''input:('This     is  ..   .     SO   ...   .   weird  . . . .     ')''')
    expectedoutput = 3
    actualoutput = count_ellipses('This     is  ..   .     SO   ...   .   weird  . . . .     ')
    print('expected output:', expectedoutput)
    print('actual output:', actualoutput)
    print('pass/fail:', passorfail(expectedoutput,actualoutput))
    print(divider)
    print("Check function output types")
    print( 'get_punctuation output type is OK',isinstance(  get_punctuation( "a", "."), str))
    print( 'analyze_punctuation output typ is OK',isinstance( analyze_punctuation( ".", "."), list))
    print( 'display_punctuation_stats output type is OK', isinstance(display_punctuation_stats( [] ), str))
    print( 'count_ellipses output type is OK', isinstance(count_ellipses( "text "), int))


if __name__ == '__main__':
    main()
