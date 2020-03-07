# -------------- Exercise 8 ----------------------------------------------------
#  Write a program that lists all subsets of the set {a, b, c, d}.

# -------------- Code  ---------------------------------------------------------
# original set
mainSet = {'a','b','c','d'}
# copy of the mainSet
mainSet_copy = mainSet.copy()
# declaring subset array
subset = []

print('All subsets of an set: ', mainSet_copy)
# i is current element in mainSet -> i = 'a', i = 'b',...
for i in mainSet:
    # then remove the current element fe. 'a' in the mainSet_copy -> than we have {'b','c','d'}
    mainSet_copy.remove(i)
    # loop over mainSet_copy set, to append all elements to subset array
    for j in mainSet_copy:
        subset.append(j)
    # and than printing the subset
    print(subset)
    # now we copy one more time the mainSet, to add the removed element
    mainSet_copy = mainSet.copy()
    # the subset array is now empty, and wait for next iteration
    subset = []