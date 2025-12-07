import sys

def calculate_z_value(s):
    """
    Computes the Z-array for a given string.

    The Z-array for a string s is an array where z[i] represents the length of the longest substring 
    starting from s[i] that matches the prefix of s.

    Parameters:
        s (str): The input string.

    Returns:
        List[int]: A list of integers representing the Z-values for each position in s.

    Time Complexity:
        O(n), where n is the length of the string.
    """
    n = len(s)
    z = [0] * n
    l, r = 0, 0

    # Loop through the string to calculate the Z values
    for k in range(1, n):

        # Case 1: If k is outside the current Z-box, compute z[k] using naive algorithm by explicit comparison
        if k > r:
            z_value = 0
            while k + z_value < n and s[z_value] == s[k + z_value]:
                z_value += 1
            z[k] = z_value
            if z_value > 0:
                l, r = k, k + z_value - 1

        # Case 2: If k is inside the current Z-box, use the Z-box values to compute z[k] more efficiently
        else:
            p = k - l # Corresponding index in the Z-box
            remaining_zbox_len = r - k + 1 # Remaining length of the Z-box

            # Case 2a (<): Copy z[k] = z[p] without checking since the match stays entirely inside the Z-box
            if z[p] < remaining_zbox_len:
                z[k] = z[p]
            
            # Case 2b (=): Extend the Z-box by explicit comparison, since the match may continue beyond r
            elif z[p] == remaining_zbox_len:
                z_value = remaining_zbox_len
                while r + 1 < n and s[r + 1] == s[z_value]:
                    r += 1
                    z_value += 1
                z[k] = r - k + 1
                l, r = k, r
            
            # Case 2c (>): Set z[k] = right_part_length to avoid checking beyond the verified Z-box
            else:
                z[k] = remaining_zbox_len

    return z


def reverse_string(s):
    """
    Reverses a given string.

    Parameters:
        s (str): The input string.

    Returns:
        str: The reversed string.

    Time Complexity:
        O(n), where n is the length of the string.
    """
    s_list = list(s) 
    left = 0
    right = len(s_list) - 1

    while left < right:
        s_list[left], s_list[right] = s_list[right], s_list[left]
        left += 1
        right -= 1

    return ''.join(s_list)


def reverse_list(lst):
    """
    Reverses a given list.

    Parameters:
        lst (List): The input list.

    Returns:
        List: The reversed list.

    Time Complexity:
        O(n), where n is the length of the list.
    """
    left = 0
    right = len(lst) - 1

    while left < right:
        lst[left], lst[right] = lst[right], lst[left]
        left += 1
        right -= 1
        
    return lst


def bad_character_table_for_binary(pattern):
    """
    Constructs the bad character table for the Boyer-Moore string matching algorithm for binary strings.

    Parameters:
        pattern (str): The pattern string for which the bad character table is built.

    Returns:
        List[List[int]]: A 2D list where index 0 corresponds to '0' and index 1 to '1'. Each row contains the 
                         last seen position of that character up to each index in the pattern.

    Time Complexity:
        O(m), where m is the length of the pattern.
    """
    m = len(pattern)

    # R[0] for '0', R[1] for '1'
    R = [[-1] * m for _ in range(2)]

    # Initialize last seen indices
    prev_value = [-1, -1]

    for j in range(m):

        # Update the last occurrence of the current character
        if pattern[j] == '0':
            prev_value[0] = j
        else:
            prev_value[1] = j

        # Copy last occurence values to R
        R[0][j] = prev_value[0]
        R[1][j] = prev_value[1]

    return R


def block_bad_character_table_with_rolling_hash(pattern, block_size):
    """
    Constructs a block-based bad character table using arithmetic-based rolling hash.

    This version treats groups of bits (blocks) as a unit to improve bad character shift performance 
    in binary strings where traditional character-level shifts are less effective due to low variety.
    It uses arithmetic (rolling) hash computation to extract binary blocks more efficiently.

    Parameters:
        pattern (str): Binary string pattern
        block_size (int): Size of the block window

    Returns:
        Dict[int, List[int]]: Maps each block's integer value to a list of rightmost occurrences 
                              up to each position.

    Time Complexity:
        O(m), where m is the length of the pattern.
    """
    m = len(pattern)

    table = {}
    prev_value = {}

    window_limit = 2 ** block_size

    # Compute the first block value as a binary integer
    block_val = int(pattern[0:block_size], 2)

    for i in range(m - block_size + 1):

        # Arithmetic rolling hash: shift left by 1 bit and add the next bit from the pattern
        if i > 0:
            next_bit = int(pattern[i + block_size - 1])
            block_val = (block_val * 2 + next_bit) % window_limit

        # Update the last occurrence of the current character
        prev_value[block_val] = i

        # Initialize table entry for the current block value if it doesn't exist
        if block_val not in table:
            table[block_val] = [-1] * (m - block_size + 1)

        # Copy last occurrence values to the table
        for j in prev_value:
            table[j][i] = prev_value[j]

    return table


def good_suffix_array(pattern):
    """
    Constructs the good suffix table for the Boyer-Moore string matching algorithm.

    Parameters:
        pattern (str): The pattern string for which the good suffix table is built.

    Returns:
        List[int]: Good suffix table for the pattern string.

    Time Complexity:
        O(m), where m is the length of the pattern.
    """
    m = len(pattern)

    # Initialize the good suffix table
    good_suffix = [None] * (m + 1)

    # Calculate the Z-values for the reversed pattern
    reversed_pattern = reverse_string(pattern)
    z_rev = calculate_z_value(reversed_pattern)
    z_rev = reverse_list(z_rev)

    # Build the good suffix table using Z-values of the reversed pattern
    for j in range(1, m - 1):
        length_of_suffix = z_rev[j]
        good_suffix[m - length_of_suffix] = j

    return good_suffix


def matched_prefix_array(pattern):
    """
    Constructs the matched prefix table for the Boyer-Moore string matching algorithm.

    Parameters:
        pattern (str): The pattern string for which the matched prefix table is built.

    Returns:
        List[int]: Matched prefix table for the pattern string.

    Time Complexity:
        O(m), where m is the length of the pattern.
    """
    m = len(pattern)

    # Calculate the Z-values for the pattern
    z_array = calculate_z_value(pattern)
    matched_prefix = [0] * (m + 1)
    
    # Loop through in reverse to calculate matched prefix values
    for j in range(m - 1, -1, -1):  

        if j + z_array[j] == m:
            matched_prefix[j] = z_array[j]
        else:
            matched_prefix[j] = matched_prefix[j + 1]

    matched_prefix[0] = m
    
    return matched_prefix


def boyer_moore_for_binary(text, pattern):
    """
    Implementation of an optimized Boyer-Moore string matching algorithm for binary strings.

    This still uses bad character and good suffix, but the bad character is extended to use  a block-based 
    table for binary strings. The good suffix rule is also optimized to skip one additional character when 
    a suffix match is found. 

    Parameters:
        text (str): Binary string text
        pattern (str): Binary string pattern

    Returns:
        List[int]: A list of starting positions of the pattern in the text in 1-indexing format.

    Time Complexity:
        Worst case:
        O(m + mn), where m is the length of the pattern and n is the length of the text. The m time comes from the
        construction of the bad character tables, and the computation of good suffix and matched prefix arrays, and 
        mn comes from the main search loop. The mn time is if Occurs when the pattern is frequent or near the end of 
        the text, causing repeated full comparisons, forcing the algorithm to check each character in the text.

        Best case:
        O(m + n/m), where m is the length of the pattern and n is the length of the text. The m time comes from the
        construction of the bad character tables, and the computation of good suffix and matched prefix arrays, and
        n/m comes from the main search loop. The n/m time is if there are many shifts, causing the algorithm to skip
        large portions of the text, leading to fewer comparisons.
    """
    m = len(pattern)
    n = len(text)

    # Return empty list if pattern is empty
    if m == 0:
        return []

    # Compute the normal bad character table
    normal_bad_char = bad_character_table_for_binary(pattern)

    # Compute the block-based bad character table with block size of 5
    block_size = 5
    block_bc = block_bad_character_table_with_rolling_hash(pattern, block_size)

    # Compute the good suffix and matched prefix arrays
    good_suffix = good_suffix_array(pattern)
    matched_prefix = matched_prefix_array(pattern)

    occurrences = []
    i = 0

    compare = 0
    shifts = 0

    # Initialize Galil's optimization variables
    galil_start = 0
    galil_end = -1

    while i <= n - m:
        j = m - 1

        shifts += 1

        while j >= 0:
            # Skip comparison if within Galil-matched region
            if galil_start <= j <= galil_end:
                j = galil_start - 1

            # Compare characters and move left when a match occurs
            elif pattern[j] == text[i + j]:
                compare += 1
                j -= 1

            # When a mismatch occurs, break the loop
            else:
                compare += 1
                break

        # If the entire pattern matched the current window in the text, an occurrence is found
        if j < 0:
            occurrences.append(i + 1)

            # Shift using matched prefix
            shift = m - matched_prefix[1]
            i += shift

            # Update Galil's optimization variables for the next iteration
            galil_start = 0
            galil_end = m - shift - 1

        # Else, the current window does not match the pattern
        else:

            # Reset Galil's optimization variables
            galil_start = 0
            galil_end = -1

            # Bad character rule
            if j >= block_size - 1:
                block_start = j - block_size + 1

                # Compute the block value for the current mismatch with CONSTANT bitwise operation
                block_val = (
                    int(text[i + block_start])     * 16 +  # 2^4
                    int(text[i + block_start + 1]) * 8 +   # 2^3
                    int(text[i + block_start + 2]) * 4 +   # 2^2
                    int(text[i + block_start + 3]) * 2 +   # 2^1
                    int(text[i + block_start + 4])         # 2^0
                )

                # If the block value exists in the table, shift applies based on the rightmost occurrence
                if block_val in block_bc and block_bc[block_val][block_start] != -1:
                    bc_shift = block_start - block_bc[block_val][block_start]

                    # Update Galil's optimization variables to skip the confirmed matched block region
                    BC_galil_start = block_bc[block_val][block_start]
                    BC_galil_end = block_bc[block_val][block_start] + block_size - 1

                # If the block value does not exist in the table, move past the mismatching block
                else:
                    bc_shift = block_start + 1

                    # Galil is not applicable in this case
                    BC_galil_start = 0
                    BC_galil_end = -1
            
            # If the region is smaller than the block size, use the normal bad character table
            else:
                mismatch_char = int(text[i + j])
                bc_shift = j - normal_bad_char[mismatch_char][j]

                # Galil is not applicable in this case
                BC_galil_start = 0
                BC_galil_end = -1

            # Good suffix rule
            if j < m - 1:

                # If a suffix match exists, shift based on the good suffix rule
                if good_suffix[j + 1] != None:
                    gs_shift = m - good_suffix[j + 1] - 1

                    # Update Galil's optimization variables to skip the confirmed matched suffix region
                    matched = m - (j + 1)
                    GS_galil_start = j + 1 - gs_shift - 1
                    GS_galil_end = GS_galil_start + matched - 1

                # Matched prefix rule when good suffix is not applicable
                else:
                    gs_shift = m - matched_prefix[j + 1]

                    # Update Galil's optimization variables to skip the confirmed matched prefix region
                    matched = matched_prefix[j + 1]
                    GS_galil_start = 0
                    GS_galil_end = matched - 1

            # If mismatch occurs at the last character, no good suffix exists, shift by 1
            else:
                gs_shift = 1
                matched = 0
                
                GS_galil_start = 0
                GS_galil_end = -1

            # Determine the shift based on the maximum of bad character and good suffix rules, and set
            # the Galil's optimization variables accordingly
            if bc_shift > gs_shift:
                shift = bc_shift
                galil_start = BC_galil_start
                galil_end = BC_galil_end

            else:
                shift = gs_shift
                galil_start = GS_galil_start
                galil_end = GS_galil_end

            # Increment the window by the bigger shift
            i += shift
            
    print("Number of comparisons :", compare)
    print("Number of shifts :", shifts)
    return occurrences


def read_file(file_path: str) -> str:
    f = open(file_path, 'r')
    line = f.readlines()
    f.close()
    return line


if __name__ == "__main__":
    _, filename1, filename2 = sys.argv
    print("Number of arguments passed :", len(sys.argv))

    print("First argument :", filename1)
    print("Second argument :", filename2)

    text = read_file(filename1)
    print("\nContent of first file :", text[0])

    pattern = read_file(filename2)
    print("\nContent of second file :", pattern[0])

    boyer_moore_for_binary = boyer_moore_for_binary(text[0], pattern[0])

    output_file = "output_a1q2.txt"
    f = open(output_file, "w")

    for position_in_txt in boyer_moore_for_binary:
        f.write(f"{position_in_txt}\n")

    f.close()