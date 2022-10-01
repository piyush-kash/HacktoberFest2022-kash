

//Program to check if variable(no) is a palindrome
public class Palindrone{
    public static void main(String[] args) {
    int no=121;
    int temp=no;
    int reverse=0;
    int remainder;

    while(temp != 0){
        remainder=temp%10;
        reverse = reverse *10+remainder;
        temp = temp/10;
    }
    
    if(no==reverse){
        System.out.println("num is palindrone");
    }else{
        System.out.println("num is not palindrone");
    }   
    }
}