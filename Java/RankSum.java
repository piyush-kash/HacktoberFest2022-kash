// Program to calculate the sum in a range of numbers; 
// Based on Gaussian formula for adding n numbers 

public class RankSum {
  public static void main(String[] args) {
    int starRange = 1, endRange = 100;

    int min = Math.min(starRange, endRange);
    int max = Math.max(starRange, endRange);
    int result = (max + min) * (max + 1 - min) / 2;

    System.out.printf("Star of Range: %d - End of Range: %d\n", starRange, endRange);
    System.out.printf("Summing result: %d", result);
  }

}
