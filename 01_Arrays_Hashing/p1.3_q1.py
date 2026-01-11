# 给定一个实数序列，设计一个最有效的算法 找到一个总和最大的区间 (extension of p53_maximum_subarray_sum)
# Input: nums = [1.5, -12.3, 3.2, -5.5, 23.2,3.2, -1.4, -62.2, 44.2, 5.4, -7.8, 1.1, -4.9]
# Output: (49.6, [8, 9])

def max_subarray_sum(nums):
    curr_sum = 0 # Invariant: maximum subarray sum ending in i
    max_sum = nums[0]
    start = 0
    end = 0
    temp_start = 0
    for i in range(len(nums)):
        if curr_sum < 0:
            curr_sum = nums[i]
            temp_start = i
        else:
            curr_sum += nums[i]
        if curr_sum > max_sum:
            max_sum = curr_sum
            start = temp_start
            end = i
    return max_sum, start, end

if __name__ == '__main__':
    print(max_subarray_sum([1.5, -12.3, 3.2, -5.5, 23.2,3.2, -1.4, -62.2, 44.2, 5.4, -7.8, 1.1, -4.9]))
    print(max_subarray_sum([-5, -2, -9]))
    print(max_subarray_sum([1, -3, 4]))
    print(max_subarray_sum([-5, 10]))