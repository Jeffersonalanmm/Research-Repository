import java.util.Random;

public class Codeium {

    /**
     * Sorts an array of integers using the Mergesort algorithm.
     *
     * @param arr the array to be sorted
     * @return the sorted array
     */
    public static int[] mergeSort(int[] arr) {
        if (arr.length <= 1) {
            return arr;
        }

        int mid = arr.length / 2;
        int[] left = new int[mid];
        int[] right = new int[arr.length - mid];

        System.arraycopy(arr, 0, left, 0, mid);
        System.arraycopy(arr, mid, right, 0, arr.length - mid);

        left = mergeSort(left);
        right = mergeSort(right);

        return merge(left, right);
    }

    /**
     * Merges two sorted arrays into a single sorted array.
     *
     * @param left  the first sorted array
     * @param right the second sorted array
     * @return the merged sorted array
     */
    private static int[] merge(int[] left, int[] right) {
        int[] result = new int[left.length + right.length];
        int i = 0, j = 0, k = 0;

        while (i < left.length && j < right.length) {
            if (left[i] <= right[j]) {
                result[k++] = left[i++];
            } else {
                result[k++] = right[j++];
            }
        }

        while (i < left.length) {
            result[k++] = left[i++];
        }

        while (j < right.length) {
            result[k++] = right[j++];
        }

        return result;
    }

    public static void main(String[] args) {
        Random rand = new Random();
        int size = 1000;
        int[] arr = new int[size];

        // Generate 1000 random values
        for (int i = 0; i < size; i++) {
            arr[i] = rand.nextInt(10000); // Random values between 0 and 9999
        }

        mergeSort(arr);
        
        // No print statements as requested
    }
}