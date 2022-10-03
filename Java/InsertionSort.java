package searching_and_sorting;

import java.util.Arrays;

public class InsertionSort {

    static void insertionSort(int[] arr){
        for (int i = 1; i < arr.length; i++){
            int j = i - 1;
            int temp = arr[i];
            while (j >= 0 && arr[j] > temp){
                arr[j+1] = arr[j];
                j--;
            }
            arr[j+1] = temp;
        }
    }

    public static void main(String[] args) {
        int[] arr = {6,4,3,5,2};
        insertionSort(arr);
        System.out.println(Arrays.toString(arr));
    }
}
