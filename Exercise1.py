# -------------- Exercise 1 ----------------------------------------------------
# Ask the user for a number. Check if the input is an integer. Depending on whether
# the number is odd or even, print out an appropriate message to the user.

# -------------- Code ----------------------------------------------------------
# taking input as long as it is in digital form
while True:
    # if input string is digit, convert it into intiger
    try:
        val = int(input('Enter a number: '))
        break
    # if not print an error
    except ValueError:
        print('That was no valid number. Try again...')
    
# checking if "val" is an intiger
print('The input number', val ,'is intiger:', isinstance(val, int))

# checking if "val" is odd or even
if ( val % 2 == 0 ):
    print('The number', val ,'is: odd')
else: 
    print('The number', val ,'is: even') 

