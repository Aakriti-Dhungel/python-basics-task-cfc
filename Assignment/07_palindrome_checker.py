# using function
def is_palindrome(s):
    rev = ''
    for char in s:
        rev = char + rev  
    return s == rev

n = input("Enter string to check if it's a palindrome: ")

if is_palindrome(n):
    print("Yes, the string is a palindrome.")
else:
    print("No, the string is not a palindrome.")



"""
#Without using function
n = input("Enter string to check palindrome or not: ")
rev = ''
for char in n:
    rev = char + rev
if n == rev:
    print("Yes, string is palindrome")
else:
    print("No,string is not palindrome")

   """