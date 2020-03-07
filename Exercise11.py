# -------------- Exercise 11 ----------------------------------------------------
# From a given list of integers remove all negative numbers

# -------------- Code  ---------------------------------------------------------
def negRemover():
    # declaring the input_num
    input_num = []
    while True:
        try:
            # catxhing the number of numbers the user want to add to the list
            list_len = (int(input('Enter a number of numbers you want to add to list: ')))
            try:
                # adding the numbers in loop as long as we have all list_len numbers
                for i in range(list_len):
                    input_num.append(int(input('Enter a numbers positive and negative: ')))
                break
            except:
                print('Error, put a number.')
            break
        except:
            print('Error, put a number.')

    
    print('Entered list: ', input_num)
    # iterating throught the elements od input_num
    for i in input_num:
        # if the i element is smaller than 0
        if (i < 0):
            # then remove it from the input_num
            input_num.remove(i)
        
    print('Output list with positive numbers and zero only: ', input_num)

negRemover()