s1=int(input("Enter Side 1 : "))
s2=int(input("Enter Side 2 : "))
s3=int(input("Enter Side 3 : "))
if s1==s2==s3:
    print("Equilateral Triangle")
elif s1!=s2!=s3:
    print("Scalene Triangle")
else:
    print("Isoceles Triangle")