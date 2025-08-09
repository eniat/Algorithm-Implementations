def duplicate_remove(A):

    # Initializing B array with -1's to track first occurrences 0-1000
    B = [-1] * (1000 +1)

    # Keeps the position to write unique elements to
    i = 0

    # Goes through the A array checking if a number is unique and moves it to the front
    for num in A:
        if B[num] == -1: #Checking it's the first occurrence
            B[num] = i # Store position
            A[i] = num # move it to the front/ new position
            i +=1 # Move on

    # removes all the excess duplicates
    del A[i:]

    return A


input_array = [0, 0, 4, 3, 12, 1, 5, 5, 3, 9, 4, 5, 32, 34, 5, 3, 2, 3, 5, 46, 3, 43,2, 5, 4, 999, 999, 1000, 1000]

print(duplicate_remove(input_array))
