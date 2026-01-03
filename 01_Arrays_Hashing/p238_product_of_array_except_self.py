# Input: nums = [1, 2, 3, 4]
# Output: [24, 12, 8, 6]

def product_of_array_except_self(arr):
    n = len(arr)
    res = [1] * n
    left = 1
    for i in range(n): # left-pass
        res[i] = left
        left *= arr[i]
    right = 1
    for j in range(n-1, -1, -1):
        res[j] = res[j] * right
        right *= arr[j]
    return res

if __name__ == '__main__':
    print(product_of_array_except_self([1, 2, 3, 4]))
    print(product_of_array_except_self([-1,1,0,-3,3]))