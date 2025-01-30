# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers. Given a string s, return true if it is a palindrome, or false otherwise.
s = input("Enter a string:")

# lowercase conversion and non-alphanumeric removal
cleaned_str = ''.join(char.lower() for char in s if char.isalnum()) 

# reverse using slicing
if cleaned_str == cleaned_str[::-1]: 
    print(True)
else:
    print(False)
