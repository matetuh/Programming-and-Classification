# -------------- Exercise 12 ----------------------------------------------------
# From a list of strings remove all strings longer than 5.

# -------------- Code  ---------------------------------------------------------


def toLongRemover():
    # declaring the input_str
    input_str = []
    while True:
        try:
            # catching the number of str the user want to add to the list
            list_len = int(input('Enter a number of strings you want to add to list: '))
            try:
                # adding the strs in loop as long as we have all list_len strs
                for i in range(list_len):
                    input_str.append(input('Enter a strings: '))
            except:
                print('Error, something iss wrong.')
            break
        except:
            print('Error, something iss wrong.')

    
    print('Entered list: ', input_str)
    for i in input_str:
        if len(i) > 5:
            input_str.remove(i)
        
    print('Output list with strings length lower than 5: ', input_str)

toLongRemover()
