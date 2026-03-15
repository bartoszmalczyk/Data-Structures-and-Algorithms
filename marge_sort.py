def mergeSort(array):
    length = len(array)
    if length <= 1:
        return
    mid = length // 2
    leftArray = array[:mid]
    rightArray = array[mid:]
    mergeSort(leftArray)
    mergeSort(rightArray)
    merge(leftArray, rightArray, array)

def merge(leftArray, rightArray, array):
    leftSize = len(leftArray)
    rightSize = len(rightArray)
    i, l, r = 0, 0, 0
    while l < leftSize and r <  rightSize:
        if leftArray[l] < rightArray[r]:
            array[i] = leftArray[l]
            l+=1
        else:
            array[i] = rightArray[r]
            r += 1
        i += 1
    while l < leftSize:
        array[i] = leftArray[l]
        i += 1
        l += 1
    while r < rightSize:
        array[i] = rightArray[r]
        i += 1
        r += 1
    


nums = [8, 2, 5, 3, 4, 7, 6, 1]
mergeSort(nums)
print(nums)