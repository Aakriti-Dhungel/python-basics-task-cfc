def sum_of_list(numbers):
    total = 0
    for num in numbers:
        total += num
    return total
my_list = [10, 20, 30, 40]
result = sum_of_list(my_list)
print(f"Sum of the list elements: {result}")
