# Part 2: Binary Search Implementation
# Implemented by: Jigme Choden Ghalley
# Pair programming parthner: Pema Checki implements

def binary_search_iterative(arr, target):
    left, right = 0, len(arr) - 1
    comparisons = 0

    while left <= right:
        comparisons += 1
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid, comparisons
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1, comparisons


def binary_search_recursive(arr, target, left=0, right=None, comparisons=0):
    if right is None:
        right = len(arr) - 1

    if left > right:
        return -1, comparisons

    comparisons += 1
    mid = (left + right) // 2

    if arr[mid] == target:
        return mid, comparisons
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right, comparisons)
    else:
        return binary_search_recursive(arr, target, left, mid - 1, comparisons)


# Example usage
if __name__ == "__main__":
    sorted_list = [12, 0, 4, 86, 67, 89]
    target = 67

    print("Sorted List:", sorted_list)
    print("Searching for", target, "using Binary Search (Iterative)")
    index, comps = binary_search_iterative(sorted_list, target)
    if index != -1:
        print("Found at index", index)
    else:
        print("Not found")
    print("Number of comparisons:", comps)

    print("\nSearching for", target, "using Binary Search (Recursive)")
    index, comps = binary_search_recursive(sorted_list, target)
    if index != -1:
        print("Found at index", index)
    else:
        print("Not found")
    print("Number of comparisons:", comps)
