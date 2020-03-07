# -------------- Exercise 14 ----------------------------------------------------
# Construct a function that constructs a list that keeps alternately consecutive elements from two argument lists of equal length. For example, for a=[a1,a2,a3] and
# a=[b1,b2,b3] the correct output is [a1,b1,a2,b2,a3,b3] .

# -------------- Code  ---------------------------------------------------------

def listConstr():
    # declaring the input_str
    a = []
    b = []
    addingList = []
    while True:
        try:
            # catching the length of lists
            list_len = int(input('Enter a length of two list - a, b : '))
            try:
                # adding list_len elements to list a and b
                for i in range(list_len):
                    # appending elements to lists
                    a.append(input('Enter a ' + str(i) + ' element to list a: '))
                    b.append(input('Enter a ' + str(i) + ' element to list b: '))
                break
            except:
                print('Error, something iss wrong.')
            break
        except:
            print('Error, something iss wrong.')

    # looping throught the a and b lists
    for i in range(list_len):
        # appending addingList with the a1,b1; a2,b2; a3,b3...
        addingList.append(a[i])
        addingList.append(b[i])

    #returning the addingList
    return addingList
        
print('The output list is: ', listConstr())

