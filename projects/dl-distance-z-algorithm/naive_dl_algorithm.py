
# A strict DL-distance ≤ 1 validator for substrings
def true_dl_distance_le1_match(s1, s2):
    """
    Returns True if the Damerau-Levenshtein distance between s1 and s2 is ≤ 1.
    Supports substitution, insertion, deletion, and transposition.
    """
    len1, len2 = len(s1), len(s2)
    if abs(len1 - len2) > 1:
        return False

    # Exact match
    if s1 == s2:
        return True

    # Substitution
    if len1 == len2:
        diff = sum(a != b for a, b in zip(s1, s2))
        if diff == 1:
            return True
        # Transposition
        for i in range(len1 - 1):
            if (s1[i] != s2[i] or s1[i+1] != s2[i+1]) and \
               s1[i] == s2[i+1] and s1[i+1] == s2[i] and s1[:i] == s2[:i] and s1[i+2:] == s2[i+2:]:
                return True
        return False

    # Insertion or Deletion
    if len1 + 1 == len2:
        # s1 is missing one char
        for i in range(len2):
            if s1 == s2[:i] + s2[i+1:]:
                return True
    elif len1 == len2 + 1:
        # s2 is missing one char
        for i in range(len1):
            if s2 == s1[:i] + s1[i+1:]:
                return True

    return False


# # Now apply this validator across all possible substrings of the text
# def validated_dl_matches(text, pattern):
#     m = len(pattern)
#     matches = []
#     for i in range(len(text) - m + 2):  # +2 for insertions
#         for window_size in [m - 1, m, m + 1]:
#             candidate = text[i:i + window_size]
#             if len(candidate) < m - 1 or i + window_size > len(text):
#                 continue
#             if true_dl_distance_le1_match(candidate, pattern):
#                 matches.append(i + 1)  # 1-based
#                 break  # Only need one window size to match
#     return sorted(set(matches))

def validated_dl_matches(text, pattern):
    m = len(pattern)
    n = len(text)
    matches = []

    for i in range(n): 
        for window_size in [m - 1, m, m + 1]:
            if i + window_size > n or window_size < m - 1:
                continue
            candidate = text[i:i + window_size]
            if true_dl_distance_le1_match(candidate, pattern):
                matches.append(i + 1) 
                break 

    return sorted(set(matches))


if __name__ == "__main__":
    # Run on your input
    text = "jeezfjezfghezfhjprjezfwtamjezfbwjezfntjezhsjezfmwijehfsjqzfnnjerzfjkzfmjzfjeezfjezfjjezfjezzfjzefejzfjefjjefoejzf"
    pattern = "jezf"
    true_matches = validated_dl_matches(text, pattern)
    print("True matches:", true_matches)

    text = "abc"
    pattern = "xabc"
    true_matches = validated_dl_matches(text, pattern)
    print("True matches:", true_matches)

    text = "mmbybjmgmmmbyhrhemmbyzmbjmbyvcglmibyyzjmmbyohvm"
    pattern = "mmby"
    true_matches = validated_dl_matches(text, pattern)
    print("True matches:", true_matches)

    text = "aaaaaa"
    pattern = "a"
    true_matches = validated_dl_matches(text, pattern)
    print("True matches:", true_matches)

