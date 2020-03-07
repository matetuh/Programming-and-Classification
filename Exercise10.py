# -------------- Exercise 10 ----------------------------------------------------
#Convert a number represented as a sequence of decimal digits to the binary representation.

# -------------- Code  ---------------------------------------------------------
def binConv():
    while True:
        try:
            input_num = int(input('Enter sequence of decimal digits which you want convert to binary representation: '))
            break
        except:
            print('Error, something is wrong.')
    # bin function which converts int numbers to binary repr
    return bin(input_num)
print(binConv())