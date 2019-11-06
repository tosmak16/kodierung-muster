# Permutation in a String (hard)
# Given a string and a pattern, find out if the string contains any permutation of the pattern.
#
# Permutation is defined as the re-arranging of the characters of the string. For example, 'abc'
# has the following six permutations:
#
# abc
# acb
# bac
# bca
# cab
# cba
# If a string has "n" distinct characters it will have n!n! permutations.
#
# Example 1:
#
# Input: String="oidbcaf", Pattern="abc"
# Output: true
# Explanation: The string contains "bca" which is a permutation of the given pattern.
# Example 2:
#
# Input: String="odicf", Pattern="dc"
# Output: false
# Explanation: No permutation of the pattern is present in the given string as a substring.
# Example 3:
#
# Input: String="bcdxabcdy", Pattern="bcdyabcdx"
# Output: true
# Explanation: Both the string and the pattern are a permutation of each other.
# Example 4:
#
# Input: String="aaacb", Pattern="abc"
# Output: true
# Explanation: The string contains "acb" which is a permutation of the given pattern.


def find_permutation(str, pattern):
    window_start, matched = 0, 0
    char_frequency = {}

    for chr in pattern:
        if chr not in char_frequency:
            char_frequency[chr] = 0
        char_frequency[chr] += 1

    # our goal is to match all the characters from the "char_frequency" with the current window
    # try to extend the range [window_start, window_end]
    for window_end in range(len(str)):
        right_char = str[window_end]
        if char_frequency.get(right_char) is not None:
            # decrement the frequency of matched character
            char_frequency[right_char] -= 1
            if char_frequency.get(right_char) == 0:
                matched += 1

        if matched == len(char_frequency):
            return True

        # shrink the window by one character
        if window_end - window_start >= len(pattern) - 1:
            left_char = str[window_start]
            window_start += 1
            if char_frequency.get(left_char) is not None:
                if char_frequency.get(left_char) == 0:
                    matched -= 1
                char_frequency[left_char] += 1

    return False


def main():
    print('Permutation exist: ' + str(find_permutation("aaadbcaf", "abc")))
    print('Permutation exist: ' + str(find_permutation("odicf", "dc")))
    print('Permutation exist: ' + str(find_permutation("bcdxabcdy", "bcdyabcdx")))
    print('Permutation exist: ' + str(find_permutation("aaacb", "abc")))


main()

