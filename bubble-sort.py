def bubble_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        # The inner loop compares adjacent elements and swaps them if they are in the wrong order
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


# Example usage
arr = [4, 7, 2, 1, 5, 9, 3, 8, 6]
sorted_arr = bubble_sort(arr)
print("Sorted array:", sorted_arr)
