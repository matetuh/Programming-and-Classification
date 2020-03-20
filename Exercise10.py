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
    #array of binary digits
    binaryNumber = []
    binaryNumber_rev = []
    #iterator
    i = 0
    #while the number id grater than zero, do
    while (input_num > 0):
        # set i'th element of the array by modulo division (3 % 2 = 1; 6 % 2 = 0)
        binaryNumber.append(input_num % 2)
        # divide the number by two
        input_num = int(input_num / 2)
        # increase the iterator
        i = i + 1

    # so the binaryNumber is now reversed
    # we must reverse it now
    for k in range (i-1, -1, -1):
        binaryNumber_rev.append(binaryNumber[k])   
    print("binary repersentation", binaryNumber_rev) 


binConv()