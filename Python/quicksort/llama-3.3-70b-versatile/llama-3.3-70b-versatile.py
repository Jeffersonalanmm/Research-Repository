def quick_sort(arr):
    """
    Sorts an array using the Quick Sort algorithm.

    Args:
        arr (list): The input array to be sorted.

    Returns:
        list: The sorted array.
    """
    if len(arr) <= 1:
        # Base case: If the array has one or zero elements, it is already sorted.
        return arr
    else:
        # Select the pivot element (in this case, the middle element).
        pivot = arr[len(arr) // 2]

        # Divide the array into three sub-arrays: elements less than the pivot,
        # elements equal to the pivot, and elements greater than the pivot.
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]

        # Recursively sort the sub-arrays and combine the results.
        return quick_sort(left) + middle + quick_sort(right)


import random

def main():
    arr = [random.randint(0, 10000) for _ in range(1000)]
    quick_sort(arr)

if __name__ == "__main__":
    main()