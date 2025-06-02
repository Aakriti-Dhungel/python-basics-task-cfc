#Even or Odd using function
def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

num = int(input("Enter a number: "))

result = even_or_odd(num)
print("The number is", result)
