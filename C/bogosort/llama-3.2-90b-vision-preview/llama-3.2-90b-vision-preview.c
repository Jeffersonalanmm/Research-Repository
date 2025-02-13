#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// Function to check if an array is sorted
int is_sorted(int arr[], int n) {
    for (int i = 0; i < n - 1; i++) {
        if (arr[i] > arr[i + 1]) {
            return 0;
        }
    }
    return 1;
}

// Function to shuffle an array
void shuffle(int arr[], int n) {
    srand(time(NULL));
    for (int i = n - 1; i > 0; i--) {
        int j = rand() % (i + 1);
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }
}

// Function to print an array
void print_array(int arr[], int n) {
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
}

// Bogo Sort algorithm
void bogo_sort(int arr[], int n) {
    while (!is_sorted(arr, n)) {
        shuffle(arr, n);
    }
}

// Example usage
int main() {
    const int size = 1000;
    int* arr = (int*)malloc(size * sizeof(int));

    // Seed para o gerador de números aleatórios
    srand(time(NULL));

    // Gera 1000 números aleatórios entre 1 e 1000
    for (int i = 0; i < size; ++i) {
        arr[i] = rand() % 1000 + 1; // Gera números entre 1 e 1000
    }

    // Ordena o array usando Bogo Sort
    bogo_sort(arr, size);

    // Libera a memória alocada
    free(arr);

    return 0;
}