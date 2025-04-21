# Part2 : Merge Sort implementation by: Pema Cheki
# Pair programming partner : Jigme Choden Ghalley implemented quick sort(Part1)

def merge_sort(arr):
    comparisons = [0]
    accesses = [0]
    
    def merge(left, right):
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            comparisons[0] += 1
            accesses[0] += 2  # access left[i] and right[j]
            if left[i] <= right[j]:
                result.append(left[i])
                accesses[0] += 1
                i += 1
            else:
                result.append(right[j])
                accesses[0] += 1
                j += 1
        while i < len(left):
            result.append(left[i])
            accesses[0] += 1
            i += 1
        while j < len(right):
            result.append(right[j])
            accesses[0] += 1
            j += 1
        return result

    def recursive_merge_sort(lst):
        if len(lst) <= 1:
            return lst
        mid = len(lst) // 2
        left = recursive_merge_sort(lst[:mid])
        right = recursive_merge_sort(lst[mid:])
        return merge(left, right)
    
    sorted_arr = recursive_merge_sort(arr)
    return sorted_arr, comparisons[0], accesses[0]

# Example usage
if __name__ == "__main__":
    original = [38, 27, 43, 3, 9, 82, 10]
    print("Original List:", original)
    sorted_list, comps, accs = merge_sort(original)
    print("Sorted using Merge Sort:", sorted_list)
    print("Number of comparisons:", comps)
    print("Number of array accesses:", accs)
