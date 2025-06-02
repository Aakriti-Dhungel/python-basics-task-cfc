def print_triangle(rows):
    for i in range(1, rows + 1):
        print('*' * i)

num_rows = int(input("Enter the number of rows: "))
print_triangle(num_rows)
