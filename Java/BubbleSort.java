package searching_and_sorting;

import java.util.Arrays;
import java.util.Scanner;

public class BubbleSort {

    static void swap(int[] arr, int a, int b){
        int temp = arr[a];
        arr[a] = arr[b];
        arr[b] = temp;
    }

    static void bubbleSort(int[] arr){
        for (int i = 0; i < arr.length - 1; i++){
            for (int j = 0; j < arr.length - i - 1; j++){
                if (arr[j] > arr[j + 1]){
                    swap(arr, j, j + 1);
                }
            }
        }
    }

    public static void main(String[] args) {
        int n;
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter the size of array: ");
        n = scanner.nextInt();
        int[] arr = new int[n];

        for (int i = 0; i < n; i++){
            arr[i] = scanner.nextInt();
        }

        bubbleSort(arr);
        System.out.println(Arrays.toString(arr));
    }
}
