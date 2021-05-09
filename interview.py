
# Some python functions, with some errors, and some interesting patterns

def applist(mylist):
    '''To append an element to a list'''
    myList.append(10)
    print('Append:',mylist)

def listsort(mylist):
    '''To sort the list'''
    mylist.sort()

def listsert(mylist)
    '''To insert an element at a specified Index'''
    mylist.insert(5, 6)
    print('Inserting \'6\' at 5th index:',mylist)

def listop1(mylist):
    '''Do something to the list'''
    [print (i) for i in reversed(mylist)]

def listop2(mylist):
    '''Do something to the list'''
    i = len(mylist) - 1 
    while i >= 0 :
        print(mylist[i]) 
        i -= 1

# Scope function start :)
x = 'Global x'
def scope():
    '''Set some vars, return some things
        Return: str
    '''
    y = 'Local y'
    x = 'Local x'
    return(x +', '+ y)
# What does the returned string look like?

def recur(mylist):
    '''Send a thing to a place
        Parameters: myList list(str)
    '''
    if len(mylist) == 1:
        item = mylist[0]
        print("Sending to", item)
    else:
        mid = len(mylist) // 2
        first_half = mylist[:mid]
        second_half = mylist[mid:]

    recur(first_half)
    recur(second_half)

def palindrome(string)
    '''This function checks the string for palindrome
        Parameters:  string (str)
    '''
    revString = string[::-1]
    if string == revString:
        print('String is Palindrome')
    else:
        print('String is not Palindrome')

