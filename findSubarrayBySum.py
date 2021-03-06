# You're given an unsorted array arr of positive integers and a number s. Your task is to find a contiguous subarray that has a sum equal to s, and return an array containing the two integers that represent its inclusive bounds. If there are several possible answers, return the one with the smallest left bound. If there are no answers, return [-1].

# Your answer should be 1-based, making the first position of the array 1 instead of 0.

# Example

# For s = 21 and arr = [4, 8, 9, 10, 3, 8], the output should be
# findSubarrayBySum(s, arr) = [1, 3].

# The sum of elements from the 1st position to the 3rd position (1-based) is equal to 21: 4 + 8 + 9.

# For s = 15 and arr = [1, 2, 3, 1, 4, 5, 6, 7, 8, 9, 10], the output should be
# findSubarrayBySum(s, arr) = [2, 6].

# The sum of elements from the 2nd position to the 6th position (1-based) is equal to 15: 2 + 3 + 1 + 4 + 5.

# Input/Output

# [time limit] 4000ms (py)
# [input] integer s

# The sum of the subarray that you are searching for.

# Guaranteed constraints:
# 1 ≤ s ≤ 109.

# [input] array.integer arr

# The given array.

# Guaranteed constraints:
# 3 ≤ arr.length ≤ 105,
# 1 ≤ arr[i] ≤ 104.

# [output] array.integer

# An array that contains two elements that represent the left and right bounds of the subarray, respectively (1-based). If there is no such subarray, return [-1].


def findSubarrayBySum(s, arr):
    cur_sum = 0
    start = 0
    for i in range(len(arr)):
        cur_sum += arr[i]
        while cur_sum > s:
            cur_sum -= arr[start]
            start += 1

        if cur_sum == s:
            return [start+1, i+1]

    return [-1]