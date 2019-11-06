# Given a string and a pattern, find the smallest substring in the given string which has all the characters
# of the given pattern.
#
# Example 1:
#
# Input: String="aabdec", Pattern="abc"
# Output: "abdec"
# Explanation: The smallest substring having all characters of the pattern is "abdec"
# Example 2:
#
# Input: String="abdabca", Pattern="abc"
# Output: "abc"
# Explanation: The smallest substring having all characters of the pattern is "abc".
# Example 3:
#
# Input: String="adcad", Pattern="abc"
# Output: ""
# Explanation: No substring in the given string has all characters of the pattern.


def find_substring(str, pattern):
    window_start = 0
    str_len = len(str)
    pattern_len = len(pattern)
    char_frequency = {}
    matched = 0
    subarray_min_length = str_len + 1
    substr_start = 0

    for number in range(pattern_len):
        current_char = pattern[number]
        if char_frequency.get(current_char) is None:
            char_frequency[current_char] = 0
        char_frequency[current_char] += 1

    for window_end in range(str_len):

        current_char = str[window_end]
        if char_frequency.get(current_char) is not None:
            char_frequency[current_char] -= 1
            if char_frequency.get(current_char) >= 0:
                matched += 1

        while matched == pattern_len:
            if subarray_min_length > window_end - window_start + 1:
                subarray_min_length = window_end - window_start + 1
                substr_start = window_start
            left_char = str[window_start]
            window_start += 1
            if char_frequency.get(left_char) is not None:
                if char_frequency.get(left_char) == 0:
                    matched -= 1
                char_frequency[left_char] += 1

    if subarray_min_length > str_len:
        return ""
    return str[substr_start: subarray_min_length + substr_start]


def main():
    print(find_substring("aabdec", "abc"))
    print(find_substring("abdabca", "abc"))
    print(find_substring("adcad", "abc"))


main()
