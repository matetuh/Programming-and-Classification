# -------------- Exercise 4 ----------------------------------------------------
# Write a function that for a given set of integers {a, . . . , b} and an integer c lists all
# integers greater than a and smaller than b that are divisible by c.

# -------------- Code  ---------------------------------------------------------

# NOTES ------------------FROM KEYBOARD ------------------------
# inpArrayOfNumb = []
# def inputFunc():
#     # if input is digital
#     try:
#         a = int(input('Enter first item of a range of integers: '))
#         b = int(input('Enter the last item of a range of integers: '))
#         c = int(input('Enter the number greater than start of range and smaller than end of range: '))
#         break
#     # if not print an error
#     except ValueError:
#             print('That was no valid number. Try again...')
#     for (i = 2; i++; i = 5):
#         inpArrayOfNumb.append(i)
#     listaA.update(inpArrayOfNumb)

# ---------------------------------------------------------------------------

# defining an list of intigers
listA = {1,2,3,4,5,6,7,8,9}
# defining c number
c = 2
# defining function that lists all
# integers greater than a and smaller than b that are divisible by c.
def listFuncGr(listName, C):
    for i in listName:
        if (i > C  and i % C == 0):
            print(i)
# calling this function
listFuncGr(listA, c)