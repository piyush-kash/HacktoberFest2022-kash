// Program to convert Arabic numbers to Roman numbers, between 1 and 3999

public class ConvertRomanNumbers {
  public static void main(String[] args) {
    int numberToConvert = 2022;
    int arabicNumber = numberToConvert;
    int arabicNumbers[] = { 1000, 990, 900, 500, 490, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1 };
    int i = 0;

    String romanNumbers[] = { "M", "CMXC", "CM", "D", "CDXC", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I" };
    StringBuilder result = new StringBuilder();

    while (numberToConvert > 0 || arabicNumbers.length == (i - 1)) {
      while ((numberToConvert - arabicNumbers[i]) >= 0) {
        numberToConvert -= arabicNumbers[i];
        result.append(romanNumbers[i]);
      }
      i++;
    }

    System.out.println("\nArabic number: " + arabicNumber + "\nRoman number: " + result);
  }
}