/**
 * @file
 * @brief Sorting of array list using [bead
 * sort](https://en.wikipedia.org/wiki/Bead_sort)
 */
#include <stdio.h>
#include <stdlib.h>

/**
 * @addtogroup sorting Sorting algorithms
 * @{
 */
/** Create easy access of elements from a 2D matrix stored in memory as a 1D
 * array
 */
#define BEAD(i, j) beads[i * max + j]

/**
 * Displays the array, passed to this method
 * @param [in] arr array to display
 * @param [in] n number of elements in the array
 */
void display(const int *arr, int n)
{
    for (int i = 0; i < n; i++)
    {
        printf("%d ", arr[i]);
    }

    printf("\n");
}

/** This is where the sorting of the array takes place
 * @param [in,out] a array to be sorted
 * @param [in] len Array Size
 */
void bead_sort(int *a, size_t len)
{
    int i, j, max, sum;
    unsigned char *beads;

    for (i = 1, max = a[0]; i < len; i++)
        if (a[i] > max)
            max = a[i];

    beads = calloc(1, max * len);

    /* mark the beads */
    for (i = 0; i < len; i++)
        for (j = 0; j < a[i]; j++) BEAD(i, j) = 1;

    for (j = 0; j < max; j++)
    {
        /* count how many beads are on each post */
        for (sum = i = 0; i < len; i++)
        {
            sum += BEAD(i, j);
            BEAD(i, j) = 0;
        }
        /* mark bottom sum beads */
        for (i = len - sum; i < len; i++) BEAD(i, j) = 1;
    }

    for (i = 0; i < len; i++)
    {
        for (j = 0; j < max && BEAD(i, j); j++)
            ;
        a[i] = j;
    }
    free(beads);
}
/** @} */

#define ARRAY_SIZE 1000

int main(void)
{
    int i;
    int *arr = (int *)malloc(ARRAY_SIZE * sizeof(int));

    srand(time(0));
    
    // Preenche o array com valores aleatórios
    for (i = 0; i < ARRAY_SIZE; i++)
    {
        arr[i] = rand() % (ARRAY_SIZE * 10); // Valores aleatórios até 9999
    }

    // Ordena o array usando bead_sort
    bead_sort(arr, ARRAY_SIZE);

    free(arr);
    return 0;
}