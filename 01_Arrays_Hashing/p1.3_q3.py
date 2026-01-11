# 在一个二维矩阵中，寻找一个矩形的区域，使其中的数字之和达到最大值 （硅谷公司真实的面试题）
# Given an n x n matrix of positive and negative integers, find the submatrix with the largest possible sum.
# Input:
# matrix = [
#     [1,3,-1],
#     [2,3,-2],
#     [-1,-2,-3]
# ]
# Output: 9
# Explanation:
# the submatrix with the largest possible sum is:
#     [
#         [1,3],
#         [2,3]
#     ]

def find_max_subarray(nums):
    curr_sum = 0
    max_sum = float('-inf')
    for num in nums:
        if curr_sum < 0:
            curr_sum = num
        else:
            curr_sum += num
        max_sum = max(max_sum, curr_sum)
    return max_sum

def max_submatrix_sum(mat):
    rows = len(mat)
    cols = len(mat[0])
    res = float('-inf')
    for i in range(rows):
        col_sum = [0] * cols
        for j in range(i, rows):
            for k in range(cols):
                col_sum[k] += mat[j][k]
            res = max(res, find_max_subarray(col_sum))
    return res


if __name__ == '__main__':
    matrix = [
        [1,3,-1],
        [2,3,-2],
        [-1,-2,-3]
    ]
    print(max_submatrix_sum(matrix))
    print(find_max_subarray([3, 6, -3]))