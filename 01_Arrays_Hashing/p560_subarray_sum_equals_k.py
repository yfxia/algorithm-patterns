# The Task: Given an array of integers (including negatives) and an integer k,
# return the total number of continuous subarrays whose sum equals k.

def subarray_sum(arr, k):
    cum_sum = 0
    seen = {0: 1}
    res = 0
    for i, num in enumerate(arr):
        cum_sum += num
        if cum_sum - k in seen:
            res += seen[cum_sum - k]
        seen[cum_sum] = seen.get(cum_sum, 0) + 1
    return res

if __name__ == '__main__':
    print(subarray_sum([5, 0, 0], 5))