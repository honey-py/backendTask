num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
num4 = int(input("Enter fourth number: "))
num5 = int(input("Enter fifth number: "))
gcd = 1

for i in range(1, min(num1, num2, num3, num4, num5) + 1):
    if num1 % i == 0 and num2 % i == 0 and num3 % i == 0 and num4 % i == 0 and num5 % i == 0:
        gcd = i

print(gcd)

# I was literally thinking for 10 mins why this question is so easy, was rechecking stuff lol!
