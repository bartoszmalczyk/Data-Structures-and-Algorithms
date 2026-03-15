def selection_sort(nums):
    for i in range(len(nums)):
        index = -1
        for j in range(i, len(nums)):
            if nums[j] < nums[index]:
                index = j
        nums[i], nums[index] = nums[index], nums[i]
    

if __name__ == "__main__":
    arr = [64, 25, 12, -22, 324, 11]
    
    print("Original array: ", end="")
    print(arr)
    
    selection_sort(arr)
    
    print("Sorted array: ", end="")
    print(arr)

