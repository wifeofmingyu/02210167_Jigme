#02210167_LAB6.py

# ----------------------------
# Part 1: Quick Sort
# Implemented by: Jigme Choden Ghalley
# ----------------------------

def quick_sort(arr):
    comparisons = 0
    swaps = 0

    def median_of_three(low, high):
        mid = (low + high) // 2
        trio = [(arr[low], low), (arr[mid], mid), (arr[high], high)]
        trio.sort(key=lambda x: x[0])
        return trio[1][1]  # return index of median

    def partition(low, high):
        nonlocal comparisons, swaps
        pivot_index = median_of_three(low, high)
        arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
        swaps += 1
        pivot = arr[high]
        i = low - 1

        for j in range(low, high):
            comparisons += 1
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
                swaps += 1

        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        swaps += 1
        return i + 1

    def quicksort_recursive(low, high):
        if low < high:
            pi = partition(low, high)
            quicksort_recursive(low, pi - 1)
            quicksort_recursive(pi + 1, high)

    quicksort_recursive(0, len(arr) - 1)
    return arr, comparisons, swaps


if __name__ == "__main__":
    original_list = [8, 0, 43, 33, 100]
    list_to_sort = original_list.copy()

    sorted_list, num_comparisons, num_swaps = quick_sort(list_to_sort)

    print("Original List:", original_list)
    print("Sorted using Quick Sort:", sorted_list)
    print("Number of comparisons:", num_comparisons)
    print("Number of swaps:", num_swaps)
