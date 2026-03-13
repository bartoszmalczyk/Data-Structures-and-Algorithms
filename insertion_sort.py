# [23, 1, 10, 5, 2]
def insertionSort(nums):
    n = len(nums)
    for i in range(1,n):
        key = nums[i]
        j = i - 1
        print(nums)
        while j >= 0 and nums[j] > key:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = key

nums = [23, 1, 10, 5, 2]


    

"""
psuedocode:

def insertionSort(int nums[]):
    m = nums.length()
    for i in range(1, m):
        key = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > key:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = key

"""