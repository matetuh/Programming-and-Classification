# -------------- Exercise 3 ----------------------------------------------------
# Write a function that computes cosine of the angle between two d-dimensional vectors.

# -------------- Code  ---------------------------------------------------------

# importing to project numpy library
import numpy as np

# filling vectors array with vector coordinates points
def CosOfAngle(d):
    # declaring array of vectors
    vectors = []
    #input
    while True:
        # if input string is digit, convert it into intiger
        try:
            #d = int(input('Enter dimension of 2 vectors: ')) -> we can also input number of dimensions - d - from keyboard
            for i in range(2):
                vector = []
                for j in range(d):
                    vector.append(int(input('Enter a ' + str(j+1) + ' dimension point of vector '+ str(i+1) +' : ')))
                vectors.append(vector)
            break
        # if not print an error
        except ValueError:
            print('That was no valid number. Try again...')
    # dot product of two vectors
    dotPrd = np.dot(vectors[0], vectors[1])
    # vectors magnitude
    vectorMag = []
    for i in range(2):
        vectorMag.append(np.linalg.norm(vectors[i]))
    # cos of angle
    cosAlfa = dotPrd/(vectorMag[0]*vectorMag[1])
    # returning array of dimension and cos
    #return [d, cosAlfa] if we input d from 'keyboard'
    return cosAlfa

#number of dimensions of two vectors 
d = 2
# the output of CosOfAngle function for d dimensions of two vectors
output = CosOfAngle(d) 
# when we want put the number of dimensions - d - from keyboard then we must write in print str(output[0]) for d and str(output[1]) for cosOfAngle
print('Cosine of the angle  between two ' + str(d) +' dimensional vectors is: ' + str(output))