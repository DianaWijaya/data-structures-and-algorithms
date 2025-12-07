def fuse(fitmons):
    """
    Function description:
    This function is used to fuse a list of fitmons together, into 1, to return an ultimate
    cuteness score. Given a list of fitmons, each fitmon has a list of 3 values, affinity_left,
    cuteness_score, and affinity_right. The cuteness score of each fitmon must be a positive
    integer. Each fitmon can only fuse with it's adjacent fitmon, and the fused cuteness score
    is calculated with a specific equation, using the affinity, and initial cuteness of both 
    fitmons. This function returns the maximum cuteness score after fusing the fitmons.

    Approach description (if main function): 
    The function uses dynamic programming with the matrix chain multiplication method to calculate
    the maximum cuteness score after fusing all the fitmons.

    To start off, I created a 2D list to store the dynamic programming memory table, to store the
    cuteness score consecutively after each fusion. Then, the base case is stored by looping through
    the list of fitmons, and storing the initial cuteness score of each fitmon, to the memory table,
    on the diagonal index of the matrix.

    Then, I used dynamic programming to calculate the maximum cuteness score after fusing all the
    fitmons. I used the matrix chain multiplication method to loop through and process the calculations
    diagonally. Since the base case is already added, the outer loop iterates over the range of 2, and 
    the length of the list of fitmons added by 1, so that the index being reached starts from 2, to 
    make sure that it is composed of at least two matrices. The second loop iterates over the possible
    starting matrices within each chain length, determining the starting matrix for each subchain.
    Then, a calculation of j is done, to determine the ending matrix for each subchain. This is then 
    used in the inner loop, where the possible partition points within each subchain are iterated over,
    which splits the subchain into two parts, for the calculations of the fusion of the fitmons.

    Within each iteration, the fusion cuteness is calculated using the formula given, which is
    computer using the affinity score of the fusing fitmons, multiplied with the cuteness score.
    Example: cuteness_score = fitmons[i][1] * fitmons[i][2] + fitmons[i+1][1] * fitmons[i+1][0], when 
    fusing fitmon[i] and fitmon[i+1]. The calculations here is done by taking the cuteness score taken
    from the memory table, and multiplying it with the affinity score from the fitmons list. This is 
    done so that we can make use of previous calculations of cuteness score to calculate the new cuteness
    score. The operation involves makes use of the memory of the cuteness score in the matrix including
    the score of the fitmon to the left and bottom of the current fitmon being fused. Finally, the 
    memory table is updated with the new cuteness score if the new calculated cuteness score is higher
    than the previous cuteness score. 
    
    This is done to make sure that the maximum cuteness score is calculated by considering all possible 
    fusion sequences and leveraging the previously computed scores stored in the dynamic programming 
    memory table. This approach optimizes the computation by avoiding redundant calculations and 
    efficiently utilizing the memory of cuteness scores of subproblems.

    The result of the final fused cuteness score is stored in the first row and last column of the memory
    table, and is returned.

    Precondition:
        - The cuteness score of each fitmon must be a positive integer
        - Each fitmon can only fuse with it's adjacent fitmon
        - The affinity of the fusing fitmons must have the same value on the side they are fusing
        - The list of fitmons must have at least 1 fitmon
    Postcondition:
        - All the fitmons are fused into one fitmon at last

    Input:
        fitmons: The list of fitmons that are being fused together. Each fitmon in the list is
                 represented as a list of 3 values, where the first value is the affinity to the
                 left, the second value is the cuteness score, and the third value is the affinity
                 to the right.
    Return:
        cuteness score: The maximum cuteness score after fusing all the fitmons into 1, with the
                        highest possible cuteness score.

    Time complexity: 
        Complexity: O(N^3), where N is the number of fitmons in the list.
        Analysis: N is the number of fitmons in the list. The first outer loop iterates over the 
                  possible lengths of the matrix chains from 2 to N+1. The second loop iterates
                  over the possible starting matrices within each chain length, determining the 
                  starting matrix for each subchain. Lastly, the inner loop iterates over the 
                  possible partition points within each subchain, which splits the subchain into 
                  two parts, for the calculations of the fusion of the fitmons.

    Space complexity: 
        Complexity: O(N^2), where N is the number of fitmons in the list.
        Analysis: N is the number of fitmons in the list. A 2D list is used to store the dynamic
                  programming memory table, to store the cuteness score consecutively after each
                  fusion.

    Input space complexity:
        Complexity: O(N), where N is the number of fitmons in the list.
        Analysis: N is the number of fitmons in the list. The input space complexity is O(N) because
                  the list of fitmons is the only input that is stored in memory.
    """

    # The length of the list of fitmons
    no_of_fitmons = len(fitmons)

    # Auxiliary space complexity: O(N^2), where N is the number of fitmons in the list
    # Stores the dynamic programming 2D memorization table
    dp = [[0] * no_of_fitmons for _ in range(no_of_fitmons)]

    # Time complexity: O(N), where N is the number of fitmons in the list
    # Base case: Storing the initial cuteness score of each fitmon
    for i in range(no_of_fitmons):
        dp[i][i] = fitmons[i][1]

    # Dynamic Programming
    # Time complexity: O(N^3), where N is the number of fitmons in the list
    # Using the matrix chain multiplication method to iterate diagonally
    for length in range(2, no_of_fitmons + 1):
        for i in range(no_of_fitmons - length + 1):
            j = i + length - 1
            for k in range(i, j):

                # Calculation of the new cuteness score after fusing the fitmons
                # Uses memory location of the fitmons' cuteness score from previous calculations
                new_cuteness = int((dp[i][k] * fitmons[k][2]) + (dp[k+1][j] * fitmons[k+1][0]))

                # Update the cuteness score if the new calculated cuteness score is higher
                if dp[i][j] < new_cuteness:
                    dp[i][j] = new_cuteness

    # The result of the final fused cuteness score is stored here, and returned
    return dp[0][no_of_fitmons-1]