#Positive numbers filter , using function
def filter_positive(numbers):
    positive_list = []
    for num in numbers:
        if num > 0:
            positive_list.append(num)
    return positive_list

numbers = [1, -2, 3, -44, 0, 9]
print("Original list:", numbers)

positive_numbers = filter_positive(numbers)

print("Positive numbers:", positive_numbers)




# # filter positive numbers from a list , without using function
# list = [1,-2,3,44]
# print(list)
# for i in list:
#     if i%2==0:
#         list.remove(i)
# print(list)
