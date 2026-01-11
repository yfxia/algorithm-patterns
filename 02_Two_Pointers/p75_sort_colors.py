# Given an array nums with n objects colored red, white, or blue,
# sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
# You must solve this problem without using the library's sort function.
# Input: nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]

def sort_colors(nums):
    low, high = 0, len(nums) - 1
    mid = 0
    while mid <= high:
        # mid = 0 RED
        if nums[mid] == 0:
            nums[mid], nums[low] = nums[low], nums[mid]
            low += 1
            mid += 1
        # mid = 1 WHITE
        elif nums[mid] == 1:
            mid += 1
        # mid = 2 BLUE
        elif nums[mid] == 2:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1
    return nums

if __name__ == '__main__':
    nums = [2,0,2,1,1,0]
    print(sort_colors(nums))