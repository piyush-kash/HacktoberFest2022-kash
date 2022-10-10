
def ispalindrome(num):
    temp = num
    rev = 0
    while num > 0:
        rev = (rev * 10) + (num % 10)
        num = num // 10
    return rev == temp

if __name__ == "__main__":
    num = 14541
    if ispalindrome(num):
        print("Palindrome")
    else:
        print("Not Palindrome")
