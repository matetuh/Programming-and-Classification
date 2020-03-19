# -------------- Exercise 15 ----------------------------------------------------
#A list contains both integers and strings. Construct a function that sorts given list
#in such a way that at the beginning of the resulting list one gets strings in alphabetical
#order followed by integers in an increasing order.

# -------------- Code  ---------------------------------------------------------

def sorting():
    # declaring the input_str
    inputs = []
    while True:
        try:
            # input_str length - 1
            list_len = int(input('Enter a number of strings which You want to enter: '))
            try:
                # appending the input
                for i in range(list_len):
                    inputs.append(input('Enter a string which contains numbers and strings: '))
            except:
                print('Error, something iss wrong.')
            break
        except:
            print('Error, something iss wrong.')
    # list of numbers and strings
    num = []
    num_sorted = []
    st = []
    #st_sorted = []
    # podział na liczby i znaki
    for i in inputs:
        if (i.isdigit()):
            num.append(int(i))
        else:
            st.append(i)
     #sorting numbers 
    for j in range(len(num)):
        for i in num  :
            if i == min(num):
                num_sorted.append(i)
                num.remove(i)
    #sorting alphabetically 
    st.sort()
    #sumowanie dwóch tablic
    outprint = st + num_sorted
    #druk
    print(outprint)
sorting()