#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// Function to merge two sorted subarrays
void merge(int arr[], int left, int mid, int right) {
    int n1 = mid - left + 1;
    int n2 = right - mid;

    // Create temporary arrays
    int left_arr[n1], right_arr[n2];

    // Copy data to temporary arrays
    for (int i = 0; i < n1; i++)
        left_arr[i] = arr[left + i];
    for (int j = 0; j < n2; j++)
        right_arr[j] = arr[mid + 1 + j];

    // Merge the temporary arrays back into arr[left..right]
    int i = 0, j = 0, k = left;
    while (i < n1 && j < n2) {
        if (left_arr[i] <= right_arr[j]) {
            arr[k] = left_arr[i];
            i++;
        } else {
            arr[k] = right_arr[j];
            j++;
        }
        k++;
    }

    // Copy the remaining elements of left_arr[], if there are any
    while (i < n1) {
        arr[k] = left_arr[i];
        i++;
        k++;
    }

    // Copy the remaining elements of right_arr[], if there are any
    while (j < n2) {
        arr[k] = right_arr[j];
        j++;
        k++;
    }
}

// Function to implement merge sort
void merge_sort(int arr[], int left, int right) {
    if (left < right) {
        int mid = left + (right - left) / 2;

        // Sort first and second halves
        merge_sort(arr, left, mid);
        merge_sort(arr, mid + 1, right);

        // Merge the sorted halves
        merge(arr, left, mid, right);
    }
}

int main() {
    // Generate a random array of 1000 integers
    srand(time(NULL));
    int arr[1000];
    for (int i = 0; i < 1000; i++)
        arr[i] = rand() % 1000;

    // Sort the array using merge sort
    merge_sort(arr, 0, 999);

    return 0;
}