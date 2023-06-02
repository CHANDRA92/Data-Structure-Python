def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    smaller = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    larger = [x for x in arr if x > pivot]

    return quick_sort(smaller) + equal + quick_sort(larger)


# Example usage
arr = [4, 7, 2, 1, 5, 9, 3, 8, 6]
sorted_arr = quick_sort(arr)
print("Sorted array:", sorted_arr)
