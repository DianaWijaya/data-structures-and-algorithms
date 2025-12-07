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

def near_exact_pattern_matching(s, pattern):
    """
    Finds all near-exact matches under the Levenshtein distance of 1 between a pattern and a text.

    Parameters:
        s (str): The input text.
        pattern (str): The input pattern.

    Returns:
        List[Tuple[int, int]]: A list of tuples where each tuple contains the starting position of 
                               the match and the type of match, in 1-indexing format.

    Time Complexity:
        O(m + n), where m is the length of the pattern and n is the length of the text.
    """
    pattern_length = len(pattern)
    text_length = len(s)

    # Constants to represent the type of match
    EXACT_MATCH = 0
    NEAR_EXACT_MATCH = 1

    # Forward pattern and string concatenation and Z-array computation
    concat = pattern + "$" + s 
    z_values = calculate_z_value(concat)[pattern_length + 1:]

    # Reversed pattern and string concatenation and reversed Z-array computation
    reversed_concat = reverse_string(pattern) + "$" + reverse_string(s)
    reversed_z_values = reverse_list(calculate_z_value(reversed_concat))[:-pattern_length - 1]

    matches = []

    for i in range(text_length - pattern_length + 2):

        # Case 1: EXACT MATCH, if z[i] is equal to the length of the pattern, then it is an exact match
        if i + pattern_length - 1 < len(reversed_z_values) and \
           z_values[i] == pattern_length:
            matches.append(((i + 1), EXACT_MATCH))

        # Case 2: INSERT, if values add up to pattern_length - 1, or more, then it is an insert operation
        elif i + pattern_length - 2 < len(reversed_z_values) and \
             pattern_length > 1 and \
             z_values[i] + reversed_z_values[i + pattern_length - 2] >= pattern_length - 1:
            matches.append(((i + 1), NEAR_EXACT_MATCH))

        # Case 3: REPLACE, if values add up to pattern_length - 1, then it is a replace operation
        elif i + pattern_length - 1 < len(reversed_z_values) and \
             z_values[i] + reversed_z_values[i + pattern_length - 1] == pattern_length - 1:
            matches.append(((i + 1), NEAR_EXACT_MATCH))

        # Case 4: SWAP, if values add up to pattern_length - 2, then it is a possible swap operation,
        # then check if the characters at the swapped positions matche the pattern
        elif i + pattern_length - 1 < len(reversed_z_values) and \
             pattern_length > 1 and \
             z_values[i] + reversed_z_values[i + pattern_length - 1] == pattern_length - 2 and \
             s[i + z_values[i]] == pattern[z_values[i] + 1] and \
             s[i + z_values[i] + 1] == pattern[z_values[i]]:
            matches.append(((i + 1), NEAR_EXACT_MATCH))

        # Case 5: DELETE, if values add up to pattern_length, or more, then it is a delete operation
        elif i < len(z_values) - pattern_length and \
             pattern_length > 1 and \
             z_values[i] + reversed_z_values[i + pattern_length] >= pattern_length:
            matches.append(((i + 1), NEAR_EXACT_MATCH))
            
    return matches

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

    near_exact_pattern_matching = near_exact_pattern_matching(text[0], pattern[0])

    output_file = "output_a1q1.txt"
    f = open(output_file, "w")

    for position_in_txt, DL_distance_with_pat in near_exact_pattern_matching:
        f.write(f"{position_in_txt} {DL_distance_with_pat}\n")

    f.close()