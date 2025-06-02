def is_prime(n):
    if n <= 1:
        return False  
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))


if is_prime(num1):
    print(num1, "is a prime number.")
else:
    print(num1, "is not a prime number.")

if is_prime(num2):
    print(num2, "is a prime number.")
else:
    print(num2, "is not a prime number.")

if is_prime(num3):
    print(num3, "is a prime number.")
else:
    print(num3, "is not a prime number.")
