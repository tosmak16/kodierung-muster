# Problem: Given a string, find the length of the longest substring in it with no more than K distinct characters.

# Example 1:
#
# Input: String="araaci", K=2
# Output: 4
# Explanation: The longest substring with no more than '2' distinct characters is "araa".
# Example 2:
#
# Input: String="araaci", K=1
# Output: 2
# Explanation: The longest substring with no more than '1' distinct characters is "aa".
# Example 3:
#
# Input: String="cbbebi", K=3
# Output: 5
# Explanation: The longest substrings with no more than '3' distinct characters are "cbbeb" & "bbebi".


def longest_substring_with_k_distinct(str, k):
    window_start = 0
    max_len = 0
    char_frequency = {}
    for window_end in range(len(str)):
        current_char = str[window_end]
        if char_frequency.get(current_char) is None:
            char_frequency[current_char] = 0
        char_frequency[current_char] += 1
        while len(char_frequency) > k:
            left_char = str[window_start]
            char_frequency[left_char] -= 1
            window_start += 1
            if char_frequency.get(left_char) == 0:
                del char_frequency[left_char]
        max_len = max(max_len, window_end - window_start + 1)
    return max_len


def main():
    print("Length of the longest substring: " + str(longest_substring_with_k_distinct("araaci", 2)))
    print("Length of the longest substring: " + str(longest_substring_with_k_distinct("araaci", 1)))
    print("Length of the longest substring: " + str(longest_substring_with_k_distinct("cbbebi", 3)))


main()
