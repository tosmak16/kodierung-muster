# Problem: Given an array, find the average of all contiguous subarrays of size ‘K’ in it.

# Solution:


def find_averages_of_subarrays(K, arr):
    result = []
    window_sum, window_start = 0.0, 0
    for windowEnd in range(len(arr)):
        window_sum += arr[windowEnd]  # add the next element
    # slide the window, we don't need to slide if we've not hit the required window size of 'k'
    if windowEnd >= K - 1:
        result.append(window_sum / K)  # calculate the average
        window_sum -= arr[window_start]  # subtract the element going out
        window_start += 1  # slide the window ahead
    return result


def main():
    result = find_averages_of_subarrays(5, [1, 3, 2, 6, -1, 4, 1, 8, 2])
    print("Averages of subarrays of size K: " + str(result))


main()
