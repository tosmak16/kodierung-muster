# String Anagrams (hard)
# Given a string and a pattern, find all anagrams of the pattern in the given string.
#
# Anagram is actually a Permutation of a string. For example, 'abc' has the following six anagrams:
#
# abc
# acb
# bac
# bca
# cab
# cba
# Write a function to return a list of starting indices of the anagrams of the pattern in the given string.
#
# Example 1:
#
# Input: String="ppqp", Pattern="pq"
# Output: [1, 2]
# Explanation: The two anagrams of the pattern in the given string are "pq" and "qp".
# Example 2:
#
# Input: String="abbcabc", Pattern="abc"
# Output: [2, 3, 4]
# Explanation: The three anagrams of the pattern in the given string are "bca", "cab", and "abc".


def find_string_anagrams(str, pattern):
    result_indexes = []
    pattern_len = len(pattern)
    str_len = len(str)
    char_frequency = {}
    window_start = 0
    matched = 0
    for item in range(pattern_len):
        current_pattern_char = pattern[item]
        if char_frequency.get(current_pattern_char) is None:
            char_frequency[current_pattern_char] = 0
        char_frequency[current_pattern_char] += 1
    for window_end in range(str_len):
        current_char = str[window_end]
        if char_frequency.get(current_char) is not None:
            char_frequency[current_char] -= 1
            if char_frequency.get(current_char) == 0:
                matched += 1

        if matched == pattern_len:
            result_indexes.append(window_start)

        if window_end >= pattern_len - 1:
            left_char = str[window_start]
            window_start += 1
            if char_frequency.get(left_char) is not None:
                if char_frequency.get(left_char) == 0:
                    matched -= 1
            char_frequency[left_char] += 1

    return result_indexes


def main():
    print(find_string_anagrams("ppqp", "pq"))
    print(find_string_anagrams("abbcabc", "abc"))


main()