num1 =int (input("Enter the range start: "))
num2 =int (input("Enter the range ends: "))
num=0
x=0
for i in range(num1,num2):
     for j in range(2,i):
        if i % j==0:
            print(i, "is Composite number")
            num = num + 1
            break
     else:
        print(i, "is Prime number")
        x = x + 1

print(x, "Prime and", num, " Composite numbers in the range.")
