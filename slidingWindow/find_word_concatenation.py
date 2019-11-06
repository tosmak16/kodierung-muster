# Words Concatenation (hard)
# Given a string and a list of words, find all the starting indices of substrings in the given string that are a
# concatenation of all the given words exactly once without any overlapping of words. It is given that all words are
# of the same length.
#
# Example 1:
#
# Input: String="catfoxcat", Words=["cat", "fox"]
# Output: [0, 3]
# Explanation: The two substring containing both the words are "catfox" & "foxcat".
# Example 2:
#
# Input: String="catcatfoxfox", Words=["cat", "fox"]
# Output: [3]
# Explanation: The only substring containing both the words is "catfox".


def find_word_concatenation(str='', words=[]):
    result_indices = []
    words_str = ''.join(words)
    char_frequency_map = {}
    words_str_len = len(words_str)
    window_start = 0
    str_len = len(str)
    matched = 0
    one_word_length = len(words[0])

    for index in range(words_str_len):
        current_char = words_str[index]
        if char_frequency_map.get(current_char) is None:
            char_frequency_map[current_char] = 0
        char_frequency_map[current_char] += 1

    for window_end in range(str_len):

        current_char = str[window_end]
        if char_frequency_map.get(current_char) is not None:
            char_frequency_map[current_char] -= 1
            if char_frequency_map.get(current_char) == 0:
                matched += 1

        if window_end - window_start == words_str_len -1:
            if matched == words_str_len:
                result_indices.append(window_start)
            counter = 0
            while one_word_length > counter:
                counter += 1

                left_char = str[window_start]
                window_start += 1
                if char_frequency_map.get(left_char) is not None:
                    if char_frequency_map.get(current_char) == 0:
                        matched -= 1
                    char_frequency_map[left_char] += 1

    return result_indices


def main():
    print(find_word_concatenation("catfoxcat", ["cat", "fox"]))
    print(find_word_concatenation("catcatfoxfox", ["cat", "fox"]))


main()

