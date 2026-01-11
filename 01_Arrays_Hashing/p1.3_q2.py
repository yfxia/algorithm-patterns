# 在一个数组中寻找一个区间，使得区间内的数字之和等于某个事先给定的数字 (extension of leetcode 560 Subarray Sum Equals K)
# Input: nums = [1,1,1], k = 2
# Output: [0,1]

def max_subarray_sum_k(nums, k):
    seen = {0:-1} # hash table of cumulative sums appear so far
    cum_sum = 0
    for i, num in enumerate(nums):
        cum_sum += num
        if cum_sum - k in seen:
            return seen[cum_sum - k] + 1, i
        seen[cum_sum] = i
    return -1, -1

if __name__ == '__main__':
    print(max_subarray_sum_k([1,1,1], 2))
    print(max_subarray_sum_k([5, 2], 2))