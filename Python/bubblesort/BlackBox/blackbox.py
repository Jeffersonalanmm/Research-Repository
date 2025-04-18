import random

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break

def main():
    random_values = [random.randint(1, 10000) for _ in range(1000)]
    bubble_sort(random_values)
    # The sorted array can be used or returned as needed
    return random_values

if __name__ == "__main__":
    sorted_values = main()