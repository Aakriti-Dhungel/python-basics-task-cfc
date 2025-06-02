def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"
    
    fact = 1
    for i in range(2, n + 1):
        fact *= i
    return fact

# User input
n = int(input("Enter a non-negative integer: "))
print(f"Factorial of {n} is: {factorial(n)}")
