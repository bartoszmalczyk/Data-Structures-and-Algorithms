def quick_sort(arr: list[int | float], start: int, end: int, version: bool):
    if end <= start:
        return
        
    if version:  
        pivot_index = lomuto_partition(arr, start, end)
        quick_sort(arr, start, pivot_index - 1, version)
        quick_sort(arr, pivot_index + 1, end, version)
    else:        
        pivot_index = hoare_partition(arr, start, end) 
        quick_sort(arr, start, pivot_index, version)
        quick_sort(arr, pivot_index + 1, end, version)


def lomuto_partition(arr: list[int | float], start: int, end: int):
    pivot = arr[end]
    i = start - 1
    for j in range(start, end):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    i += 1
    arr[i], arr[end] = arr[end], arr[i]
    return i 

def hoare_partition(arr: list[int | float], start: int, end: int):
    pivot = arr[start]
    i = start - 1
    j = end + 1
    while True:
        i += 1
        while arr[i] < pivot:
            i += 1
        j -= 1
        while arr[j] > pivot:
            j -= 1
        if i >= j: 
            return j
        arr[i], arr[j] = arr[j], arr[i]

if __name__ == "__main__":
    arr = [8, 2, 5, 3, 9, 4, 7, 6, 1]
    

    quick_sort(arr, 0, len(arr) - 1, True) 
    print("Sorted (Lomuto):", arr)
    
    arr2 = [8, 2, 5, 3, 9, 4, 7, 6, 1]
    quick_sort(arr2, 0, len(arr2) - 1, False)
    print("Sorted (Hoare): ", arr2)