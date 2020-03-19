# -------------- Exercise 13 ----------------------------------------------------
# Construct a function that returns a string of maximal length from a set of strings.
#Note that the the maximal string does not have to be unique..

# -------------- Code  ---------------------------------------------------------

def maxStr():
    # declaring the input_str
    input_str = []
    while True:
        try:
            # catxhing the number of str the user want to add to the list
            list_len = int(input('Enter a number of strings you want to add to list: '))
            try:
                # adding the strs in loop as long as we have all list_len strs
                for i in range(list_len):
                    input_str.append(input('Enter a strings: '))
                break
            except:
                print('Error, something iss wrong.')
            break
        except:
            print('Error, something iss wrong.')

    # wypisz listę input_str
    print('Entered list: ', input_str)
    # przypisz maksymalną liczbę z (długość znaków każdego elementu listy input_str)
    length = max(len(i) for i in input_str)
    # wydrukuj ".." + każdy element listy input_str jeśli długość tego elementu jest równa wartości length 
    print("Maximal length string: ", [i for i in input_str if len(i) == length])


maxStr()

