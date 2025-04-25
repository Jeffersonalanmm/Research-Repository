def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def main():
    arr = list(range(1, 1001))  # List of 1000 integers from 1 to 1000
    target = 567  # Example target to search for
    result = binary_search(arr, target)

if __name__ == "__main__":
    main()