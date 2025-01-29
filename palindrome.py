palindrome = input("Enter a word: ")

palindrome = palindrome.lower()

if palindrome == palindrome[::-1]: #reverse the word using slicing method and check whether the reversed word and original word are same
    print("It is a palindrome")
else:
    print("Not a palindrome")
 