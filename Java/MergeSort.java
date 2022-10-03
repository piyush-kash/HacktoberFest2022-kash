package searching_and_sorting;

import java.util.Arrays;

public class MergeSort {
    public static void main(String[] args) {
        int[] arr = {2, 6, 8, 5, 4, 3};
        System.out.println(Arrays.toString(arr));
        mergeSort(arr);
        System.out.println(Arrays.toString(arr));
    }

    static void mergeSort(int[] input) {
        if (input.length <= 1) {
            return;
        }
        int mid = input.length / 2;
        int[] part1 = new int[mid];
        int[] part2 = new int[input.length - mid];
        System.arraycopy(input, 0, part1, 0, mid);
        int k = 0;
        for (int i = mid; i < input.length; i++) {
            part2[k] = input[i];
            k++;
        }
        mergeSort(part1);
        mergeSort(part2);
        merge(part1, part2, input);
    }

    static void merge(int[] input1, int[] input2, int[] output) {
        int i = 0, j = 0, k = 0;
        while (i < input1.length && j < input2.length) {
            if (input1[i] < input2[j]) {
                output[k] = input1[i];
                k++;
                i++;
            } else {
                output[k] = input2[j];
                j++;
                k++;
            }
        }
        while (i < input1.length) {
            output[k] = input1[i];
            k++;
            i++;
        }
        while (j < input2.length) {
            output[k] = input2[j];
            j++;
            k++;

        }
    }
}
