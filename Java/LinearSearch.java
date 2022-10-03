package searching_and_sorting;

import java.util.Scanner;

public class LinearSearch {

    static int linearSearch(int[] arr, int element){
        for(int i = 0; i < arr.length; i++){
            if(element == arr[i]){
                return i;
            }
        }
        return -1;
    }

    public static void main(String[] args) {
        int n;
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter the size of the array: ");
        n = scanner.nextInt();

        int[] arr = new int[n];
        for (int i = 0; i < n; i++){
            arr[i] = scanner.nextInt();
        }
        System.out.print("Enter element to be searched: ");
        int element = scanner.nextInt();
        System.out.println("Element is at index: " + linearSearch(arr, element));
    }
}
