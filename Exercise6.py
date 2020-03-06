# -------------- Exercise 6 ----------------------------------------------------
# Write a function that removes all a letters form a given string x. For example, for
# x =abracadabra we expect x =brcdbr.
# -------------- Code  ---------------------------------------------------------

def Removing_a():
    #input string
    InputStr = input('Input an string in which You want to remove an "a" letter: ')
    # string.replace(a,b) return a copy of string
    OutputStr = InputStr.replace('a', '')
    return OutputStr

# printing returned value from called function Removing_a
print(Removing_a())