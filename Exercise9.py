# -------------- Exercise 9 ----------------------------------------------------
#Write a program that returns the most frequent letter in a string

# -------------- Code  ---------------------------------------------------------
# definig function which takes input and counts the most frequent letter
def popularElement():
    while True:
        try:
            input_array = input('Enter a string in which you want to count the most frequent letter: ')
            break
        except:
            print('Error, something is wrong.')
    # declaring counter which counts the popularity of letter
    counter = 0
    # declaring popular_el which catches the most popular element
    popular_el = 0
    
    for i in range (len(input_array)):
        # if the number of i elements is grater than the number of counter
        if (input_array.count(input_array[i]) > counter):
            # then counter equals the number of the i - element
            counter = input_array.count((input_array[i]))
            # popular_el catches the most popular element
            popular_el = input_array[i]
    
    print('The most popular element: ', popular_el)
    print('Number of times it repeats: ', counter)

popularElement()
