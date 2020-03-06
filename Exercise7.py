# -------------- Exercise 7 ----------------------------------------------------
# Write a program that accepts a sentence and calculates the number of letters and digits. Hint: you can use functions isalpha() and isdigit().

# -------------- Code  ---------------------------------------------------------

def CalcLetter():
    while True:
        # if input string is digit, convert it into intiger
        try: 
            sentence = input('Enter a sentence: ')
            break
        # if not print an error
        except ValueError:
            print('Try again...')
    # declaring variables
    numberOfLetters = 0
    numberOfNumbers = 0
    # for loop for iterating throught the sentence
    for i in range(len(sentence)):
        if(sentence[i].isalpha()):
            numberOfLetters += 1
        elif(sentence[i].isdigit()):
            numberOfNumbers += 1
    print(f'Number of letters in this sentence is: {numberOfLetters}')
    print(f'Number of nummbers in this sentence is: {numberOfNumbers}')

CalcLetter()