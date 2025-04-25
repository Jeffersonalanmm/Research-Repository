import random

def bead_sort(arr):
    max_value = max(arr)
    
    beads = [[0] * num for num in arr]
    
    for i in range(len(arr)):
        for j in range(arr[i]):
            beads[i][j] = 1
    
    for j in range(max_value):
        column_sum = sum(beads[i][j] for i in range(len(arr)))
        for i in range(len(arr)):
            beads[i][j] = 1 if i < column_sum else 0
    
    return [sum(row) for row in beads]

def main():
    # Generate a list of 1000 random values between 1 and 100
    arr = [random.randint(1, 100) for _ in range(1000)]
    
    # Sort the array using bead sort
    sorted_arr = bead_sort(arr)
    
    return sorted_arr

if __name__ == "__main__":
    sorted_array = main()