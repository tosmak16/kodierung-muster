# Problem Statement
# Given a string, find the length of the longest substring which has no repeating characters.
#
# Example 1:
#
# Input: String="aabccbb"
# Output: 3
# Explanation: The longest substring without any repeating characters is "abc".
# Example 2:
#
# Input: String="abbbb"
# Output: 2
# Explanation: The longest substring without any repeating characters is "ab".
# Example 3:
#
# Input: String="abccde"
# Output: 3
# Explanation: Longest substrings without any repeating characters are "abc" & "cde".


def non_repeat_substring(str):
    max_length = 0
    last_char = ''
    counter = 0
    for window_end in range(len(str)):
        current_char = str[window_end]
        if last_char != current_char:
            counter += 1
            last_char = current_char
        elif last_char == current_char:
            counter = 1
        max_length = max(max_length, counter)

    return max_length


def main():
    print("Length of the longest substring: " + str(non_repeat_substring("aabccbb")))
    print("Length of the longest substring: " + str(non_repeat_substring("abbbb")))
    print("Length of the longest substring: " + str(non_repeat_substring("abccde")))


main()