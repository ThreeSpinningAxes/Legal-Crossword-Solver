import math

# By Devraj Chudasama
# Student number: 500975539

# This is my crossword function that prints out a generated crossword given a list of words, L
# It is composed of several other helper functions


def crossword(L):

    # Initializing a 20 x 20 matrix
    matrix = [' '] * 20

    for x in range(len(matrix)):
        matrix[x] = [' '] * 20

    # Function for printing the matrix into console.
    # It contains numbers on the right and left side of the matrix that refer to index number
    # Numbers on the top after 9 refer to 10 and above respectively
    def printmatrix(matrix):

        i, j = len(matrix), len(matrix[0])
        top_bottS = ' 0 1 2 3 4 5 6 7 8 9' * 2
        top_bottSU = ' _' * 20
        print(top_bottS)
        print(top_bottSU)

        # Printing out each index of the matrix into console

        for x in range(0, i):
            for k in range(0, j):
                if k is 0:
                    print('|', end='')
                print(matrix[x][k] + ' ', end='')
                if k is 19:
                    print('|' + str(x)
                          )

        print(top_bottSU)
        print(top_bottS)

    # This function adds the first word horizontally onto the middle of the matrix
    def addFirstWord(matrix, word):

        # If the length of the word is greater then 20, return False since the word does not fit onto the matrix
        if len(word) > 20:
            return False
        else:

            # Calculates the starting index and ending indexes of where the word needs to be placed
            # Then loops through the matrix on those indexes and adds each letter of the first word

            end = 10 + (len(word)) // 2
            start = 10 - math.ceil((len(word)) / 2)

            for index in range(start, end):
                matrix[9][index] = word[index - start]

            # Returns True if word can be successfully added
            return True

    # This function is to check if the word can be placed legally at a specific row and column vertically
    def checkvertical(matrix, word, row, col):

        # Turns the word into a list of characters
        word = list(word)

        # Checks to see if the word can fit onto the matrix at that position vertically
        if len(word) > 20 - row:
            return False

        # Variable Lettermatch is used to check if a letter in word intersects with another letter on the matrix
        lettermatch = False

        # Variable to see how many number of intersections occur in sequence.
        # Used to see if placement of the word will overlap another word
        overlapcounter = 0

        # Loop that iterates over the matrix's indexes where the word can be theoretically be placed
        # Has if statements that checks if the word can be legally placed by checking the surroundings indices
        # of the letters being placed

        for x in range(len(word)):

            # reset overlap counter if the next letter on the matrix is a blank space
            if matrix[row + x][col] is ' ':
                overlapcounter = 0

            # Checks to see if the index where the current letter is being placed intersects with another letter
            # on the matrix
            if matrix[row + x][col] is word[x]:
                overlapcounter += 1
                lettermatch = True
                continue

            # If the letter apart of the word being placed into the matrix intersects with a letter that is not of the same character, return False
            if matrix[row + x][col] != ' ' and matrix[row + x][col] != word[x]:
                return False

            # If the word is being placed at column 0
            # only check the indices to the right of each letter of the word to see if any new words are created
            # if a non-blank character is next any of the letters being placed, return False
            if col is 0:

                if matrix[row + x][col + 1] != ' ':
                    return False

            # If the word is being placed at column 19
            # only check the index to the left of each letter of the word to see if any new words are created
            # if a non-blank character is next any of the letters being placed, return False
            elif col is 19:

                if matrix[row + x][col - 1] != ' ':
                    return False
            else:

                # If the word is not placed at either ends of the matrix
                # Check indices left and right of each letter of the word when placed to see
                # if any new words are created
                # If a non-blank character is next to any of the letters being placed, return False
                if matrix[row + x][col + 1] != ' ' or matrix[row + x][col - 1] != ' ':
                    return False

        # If the word is being placed at row 0 and if the length of the word is not 20
        # Check the index that is directly below the last letter of the word being placed vertically onto the matrix
        # If that index contains a non-blank character, return False
        if row is 0:

            if len(word) is not 20:

                if matrix[row + len(word)][col] != ' ':
                    return False

        # If the row the word is being placed at is at the max row that allows the word to be fully vertically placed
        # Check the index that is directly above the first letter of the word being placed vertically onto the matrix
        # If that index contains a non-blank character, return False
        elif row is (19 - (len(word) - 1)):

            if matrix[row - 1][col] != ' ':
                return False
        else:

            # If the row where the word is being placed is neither at the top or bottom side of the matrix
            # Check both the indexes directly above the first letter of the word
            # and the index below the last letter of the word
            # If either those index's contain a non-blank character, return False
            if matrix[row - 1][col] != ' ' or matrix[row + len(word)][col] != ' ':
                return False

        # Checks if there was more then 1 letter intersections that occurred in sequence
        # If there was, that means the word being placed was overlapping another already placed word
        # If this case is true, return False
        if overlapcounter > 1:
            return False

        # If the placement of the word satisfied all legal conditions
        # Return lettermatch, which should be True if there was at least one letter intersection with another word
        return lettermatch

    # Function that tries to add a word vertically to the matrix
    def addvertical(matrix, word):
        # loops through each index of the matrix and checks if it can be placed
        for row in range(20):

            for col in range(20):

                # If it can be placed legally at the specified index, then replace the needed indexes of the matrix
                # with the letters of the word
                if checkvertical(matrix, word, row, col) is True:
                    start = row
                    end = start + len(word)

                    for k in range(start, end):
                        matrix[k][col] = word[k - start]

                    # if the word can be placed, return True
                    return True

        # If the word cannot be placed anywhere on the matrix, return False
        return False

    # This function is written in a way analogous to the function checkvertical
    # Only difference is the changes made to row and col respectively in checkvertical are now switched
    # For example, changes made to row in checkvertical are now happening to col in checkhorizontal
    def checkhorizontal(matrix, word, row, col):
        word = list(word)

        if len(word) > 20 - col:
            return False

        lettermatch = False
        overlapcounter = 0

        for x in range(len(word)):

            if matrix[row][col + x] is ' ':
                overlapcounter = 0

            if matrix[row][col + x] is word[x]:
                lettermatch = True
                overlapcounter += 1
                continue

            if matrix[row][col + x] != ' ' and matrix[row][col + x] != word[x]:
                return False

            if row is 0:

                if matrix[row + 1][col + x] != ' ':
                    return False
            elif row is 19:

                if matrix[row - 1][col + x] != ' ':
                    return False
            else:

                if matrix[row + 1][col + x] != ' ' or matrix[row - 1][col + x] != ' ':
                    return False

        if col is 0:

            if len(word) is not 20:

                if matrix[row][col + len(word)] != ' ':
                    return False

        elif col is 19 - (len(word) - 1):

            if matrix[row][col - 1] != ' ':
                return False
        else:

            if matrix[row][col - 1] != ' ' or matrix[row][col + len(word)] != ' ':
                return False

        if overlapcounter > 1:
            return False

        return lettermatch

    # Function tries to add a word horizontally to the matrix
    # This function is written in a way analogous to the function addvertical
    # Only difference is the changes made to row and col respectively in addvertical are now switched
    # (except for looping through the matrix)
    def addhorizontal(matrix, word):

        for row in range(20):

            for col in range(20):

                if checkhorizontal(matrix, word, row, col) is True:

                    s = col
                    e = s + len(word)

                    for k in range(s, e):
                        matrix[row][k] = word[k - s]
                    return True
        return False

    # Loop that adds the words from the given list L onto the matrix
    for i in range(len(L)):

        # Adds the first word and continues when i is 0
        if i is 0:
            addFirstWord(matrix, L[i])
            continue

        # If the words index is odd, place the word at that index vertically
        # If it cannot be placed, print that it cant be placed into console
        if i % 2 is 1:
            if addvertical(matrix,L[i]) is True:

                # Pass since writing addvertical in the if statement already adds the word vertically onto the matrix
                pass
            else:
                print(L[i], '(word ' + str(i) + ')', 'cannot be placed legally vertically onto the grid')
        else:

            # If the words index is even, place the word at that index horizontally
            # If it cannot be placed, print that it cant be placed into console
            if addhorizontal(matrix, L[i]) is True:

                # pass is used here for the same reason it is used for if addvertical
                pass
            else:
                print(L[i],'(word ' + str(i) + ')', 'cannot be placed legally horizontal onto the grid')

    #prints the matrix into console
    printmatrix(matrix)


# Test cases
crossword(['clowning','apple', 'addle', 'loon','burr','incline','plan'])
print()
crossword(["aaa","aaa","aaa","aaa","aaa","aaa","aaa","aaa","aaa","aaa","aaa","aaa","aaa","aaa","aaa","aaa","aaa","aaa","aaa","aaa","aaa","aaa","aaa","aaa","aaa","aaa","aaa","aaa","aaa","aaa","aaa","aaa","aaa","aaa","aaa","aaa","aaa","aaa","aaa","aaa","aaa","aaa", "aaa","aaa","aaa","aaa","aaa","aaa","aaa","aaa","aaa","aaa","aaa","aaa","aaa","aaa","aaa","aaa","aaa","aaa","aaa","aaa","aaa","aaa","aaa","aaa","aaa","aaa","aaa","aaa","aaa","aaa","aaa","aaa","aaa","aaa","aaa","aaa"])

