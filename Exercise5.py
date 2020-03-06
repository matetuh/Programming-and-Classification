# -------------- Exercise 5 ----------------------------------------------------
#Write a program that for two lists x and y (possibly of different sizes) returns a list of
#elements that are common between the lists.

# -------------- Code  ---------------------------------------------------------

# two lists of diffrent sizes
x = [1,2,3,'a','b','c']
y = [3,4,5,2,'d','f','a','b','g']

# returning common elements of each set in 2 ways
def isCommon(a, b):
    return ( set(a) & set(b) )
# printing the returned list from isCommon(a,b) function
print(isCommon(x,y))

## printing common elements of each set in 2 ways
print( set(x) & set(y) )
print( set(x).intersection(y) )
