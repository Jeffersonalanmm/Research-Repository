package theAlgorithms;

import java.util.Random;

public class theAlgorithms{

    public int[] sort(int[] unsorted) {
        int n = unsorted.length;
        heapify(unsorted, n);
        while (n > 1) {
            swap(unsorted, 1, n--);
            siftDown(unsorted, 1, n);
        }
        return unsorted;
    }

    private static void heapify(int[] unsorted, int n) {
        for (int k = n / 2; k >= 1; k--) {
            siftDown(unsorted, k, n);
        }
    }

    private static void siftDown(int[] unsorted, int k, int n) {
        while (2 * k <= n) {
            int j = 2 * k;
            if (j < n && less(unsorted, j, j + 1)) {
                j++;
            }
            if (!less(unsorted, k, j)) {
                break;
            }
            swap(unsorted, k, j);
            k = j;
        }
    }

    private static void swap(int[] array, int idx, int idy) {
        int swap = array[idx - 1];
        array[idx - 1] = array[idy - 1];
        array[idy - 1] = swap;
    }

    private static boolean less(int[] array, int idx, int idy) {
        return array[idx - 1] < array[idy - 1];
    }

    public static void main(String[] args) {
        // Criando um array com 1000 valores
        int[] array = new int[1000];

        // Preenchendo o array com valores aleatórios entre 1 e 100
        Random random = new Random();
        for (int i = 0; i < array.length; i++) {
        array[i] = random.nextInt(100) + 1; // Gera um número aleatório entre 1 e 100
        }
        theAlgorithms algorithms = new theAlgorithms();

        // Chamando o método de ordenação
        algorithms.sort(array);
    }
}