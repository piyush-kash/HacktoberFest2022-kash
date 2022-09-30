package searching_and_sorting;

import java.util.Arrays;

public class SelectionSort {

    static void selectionSort(int[] arr){
        for (int i = 0; i < arr.length - 1; i++){ // 0 to length -2
            int min = arr[i];
            int minIndex = i;
            for (int j = i + 1; j < arr.length; j++){
                if (arr[j] < min){
                    min = arr[j];
                    minIndex = j;
                }
            }
            if(minIndex != i) {
                arr[minIndex] = arr[i];
                arr[i] = min;
            }
        }
    }

    public static void main(String[] args) {
        int[] arr = {1,243,0,2,4,45};
        selectionSort(arr);
        System.out.println(Arrays.toString(arr));
    }
}
