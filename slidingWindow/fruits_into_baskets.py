# Problem Statement
# Given an array of characters where each character represents a fruit tree, you are given two baskets and your goal is
# to put maximum number of fruits in each basket. The only restriction is that each basket can have only one type of
# fruit.
#
# You can start with any tree, but once you have started you can’t skip a tree. You will pick one fruit from each tree
# until you cannot, i.e., you will stop when you have to pick from a third fruit type.
#
# Write a function to return the maximum number of fruits in both the baskets.
#
# Example 1:
#
# Input: Fruit=['A', 'B', 'C', 'A', 'C']
# Output: 3
# Explanation: We can put 2 'C' in one basket and one 'A' in the other from the subarray ['C', 'A', 'C']
# Example 2:
#
# Input: Fruit=['A', 'B', 'C', 'B', 'B', 'C']
# Output: 5
# Explanation: We can put 3 'B' in one basket and two 'C' in the other basket.
# This can be done if we start with the second letter: ['B', 'C', 'B', 'B', 'C']

# Solution:


def fruits_into_baskets(fruits):
    # TODO: Write your code here

    window_start = 0
    fruit_type_frequency = {}
    count = 0
    for window_end in range(len(fruits)):
        current_fruit = fruits[window_end]
        if fruit_type_frequency.get(current_fruit) is None:
            fruit_type_frequency[current_fruit] = 0
        fruit_type_frequency[current_fruit] += 1
        if len(fruit_type_frequency) > 2:
            left_fruit = fruits[window_start]
            fruit_type_frequency[left_fruit] -= 1
            if fruit_type_frequency.get(left_fruit) == 0:
                del fruit_type_frequency[left_fruit]
            window_start += 1
        count = max(count, window_end - window_start + 1)

    return count


def main():
    print("Maximum number of fruits: " + str(fruits_into_baskets(['A', 'B', 'C', 'A', 'C'])))
    print("Maximum number of fruits: " + str(fruits_into_baskets(['A', 'B', 'C', 'B', 'B', 'C'])))


main()
