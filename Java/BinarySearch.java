package searching_and_sorting;

public class BinarySearch {

    static int binarySearch(int[] arr, int start, int end, int element) {
        int mid;
        while (start <= end){
            mid = (start + end)/2;
            if (arr[mid] == element){
                return mid;
            } else if(arr[mid] > element){
                end = mid - 1;
            } else {
                start = mid + 1;
            }
        }
        return -1;
    }

    public static void main(String[] args) {
        int[] arr = {6, 10, 15, 32, 35, 40, 45, 60};
        System.out.print(binarySearch(arr, 0, arr.length - 1, 61));
    }
}
