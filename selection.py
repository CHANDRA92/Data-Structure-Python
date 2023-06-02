def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


# Example usage
arr = [4, 7, 2, 1, 5, 9, 3, 8, 6]
sorted_arr = selection_sort(arr)
print("Sorted array:", sorted_arr)
