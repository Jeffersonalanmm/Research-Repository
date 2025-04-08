

import java.util.Arrays;
import java.util.Random;

public class BlackBox {
    static void bubbleSort(int array[]) {
    int size = array.length;
    for (int i = 0; i < size - 1; i++)
      for (int j = 0; j < size - i - 1; j++)
        if (array[j] > array[j + 1]) {
          int temp = array[j];
          array[j] = array[j + 1];
          array[j + 1] = temp;
        }
  }
public static void main(String[] args) {
    int[] array = new int[5];
    Random random = new Random();

    for (int i = 0; i < array.length; i++) {
        array[i] = random.nextInt(100) + 1;
    }

    System.out.println("Antes da ordenação:");
    System.out.println(Arrays.toString(array));

    bubbleSort(array);

    System.out.println("Depois da ordenação:");
    System.out.println(Arrays.toString(array));
}


}
