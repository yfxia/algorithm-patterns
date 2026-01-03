# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
# Input: nums = [100, 4, 200, 1, 3, 2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Its length is 4.
# Input: nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
# Output: 9

def longest_consecutive_sequence(arr):
    longest = 0
    nums_set = set(arr)
    for num in nums_set:
        if num - 1 not in nums_set:
            length = 1
            while num + length in nums_set:
                length += 1
            longest = max(longest, length)
    return longest


if __name__ == '__main__':
    print(longest_consecutive_sequence([100, 4, 200, 1, 3, 2]))
    print(longest_consecutive_sequence([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))
