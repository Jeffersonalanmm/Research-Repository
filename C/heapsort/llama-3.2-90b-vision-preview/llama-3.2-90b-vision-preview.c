#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// Function to swap two elements
void swap(int* a, int* b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

// Function to heapify the array
void heapify(int arr[], int n, int i) {
    int largest = i;
    int left = 2 * i + 1;
    int right = 2 * i + 2;

    if (left < n && arr[left] > arr[largest])
        largest = left;

    if (right < n && arr[right] > arr[largest])
        largest = right;

    if (largest != i) {
        swap(&arr[i], &arr[largest]);
        heapify(arr, n, largest);
    }
}

// Function to perform heap sort
void heapSort(int arr[], int n) {
    // Build a max heap
    for (int i = n / 2 - 1; i >= 0; i--)
        heapify(arr, n, i);

    // Extract elements one by one
    for (int i = n - 1; i >= 0; i--) {
        swap(&arr[0], &arr[i]);
        heapify(arr, i, 0);
    }
}

// Function to generate a random array
void generateRandomArray(int arr[], int n) {
    srand(time(NULL));
    for (int i = 0; i < n; i++)
        arr[i] = rand() % 1000;
}

int main() {
    int n = 1000;
    int* arr = (int*)malloc(n * sizeof(int));

    // Generate a random array
    generateRandomArray(arr, n);

    // Perform heap sort
    heapSort(arr, n);

    // Free the memory
    free(arr);

    return 0;
}