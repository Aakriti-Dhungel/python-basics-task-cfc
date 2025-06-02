
text = input("Enter a string: ")
# Reverse String
print("Reversed string:", text[::-1])

# Convert to uppercase
print("Uppercase string:", text.upper())

# Count vowels
vowels = "aeiouAEIOU"
count = 0
for ch in text:
    if ch in vowels:
        count = count + 1
print("Number of vowels:", count)
