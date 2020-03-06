# -------------- Exercise 2 ----------------------------------------------------
# Generate 20 integers in the range 10 − 99 at random and return their mean value and
# maximal value.

# -------------- Code  ---------------------------------------------------------

# importing random library
import random as rnd
import statistics as stc

# defining function that returns mean and max value of set of 20 random numbers in range 10 - 99
def MeanMaxRand():
    # declaring ranNumb array
    ranNumb = []
    # declaring mean and max array
    MeanMax = []
    # appending 20 nandom numbers in the range 10 - 99
    for i in range (20):
        ranNumb.append(rnd.randint(10, 99))
    # mean and max value adding in array MeanMax
    MeanMax.append(stc.mean(ranNumb))
    MeanMax.append(max(ranNumb))

    return MeanMax

print('The mean value of 20 integers at the range 10-99 is:', MeanMaxRand()[0])
print('The max value of 20 integers at the range 10-99 is:', MeanMaxRand()[1])