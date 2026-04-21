def quick_sort(arr: list[int | float], start: int, end: int):
    if end <= start:
        return
    pivot = partition(arr, start, end)
    quick_sort(arr, start, pivot - 1)
    quick_sort(arr, pivot + 1, end)


def partition(arr: list[int | float], start: int, end: int):
    pivot = arr[end]
    i = start - 1
    for j in range(start, end):
        if arr[j] < pivot:
            i += 1
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
    i += 1
    temp = arr[i]
    arr[i] = arr[end]
    arr[end] = temp
    return i 

if __name__ == "__main__":
    arr = [8, 2, 5, 3, 9, 4, 7, 6, 1]
    quick_sort(arr, 0, len(arr) - 1)
    print(arr)