#1.Write a program that enters two integers n and l and generates, in alphabetical order, all possible "stupid” passwords" that consist of the following 5 characters:
#Character 1: a digit from 1 to n.
#Character 2: a digit from 1 to n.
#Character 3: a small letter from the first l letters of the Latin alphabet.
#Character 4: a small letter from the first l letters of the Latin alphabet.
#Character 5: a digit from 1 to n, greater than the first 2 digits.
#Input Data
#The input is read from the console and consists of two integers: n and l within the range [1 … 9], each on a single line.

#Output Data
#Print on the console all "stupid" passwords in alphabetical order, separated by space


n = int(input("Enter any number from 0 to n"))  
l = int(input("Enter any letter from 0 to l"))  

digits = [str(i) for i in range(1, n + 1)] #getting the nums in the range and converting into a string
letters = [chr(i) for i in range(ord('a'), ord('a') + l)]  #getting the letters and converting into a character,ord is used to represent the letters as numbers

passwords = [] #list for storing the password

for d1 in digits:
    for d2 in digits:
        for c1 in letters:
            for c2 in letters:
                for d3 in digits:
                    if int(d3) > int(d1) and int(d3) > int(d2):
                        password = d1 + d2 + c1 + c2 + d3
                        passwords.append(password)

print(" ".join(sorted(passwords))) #using sort() to arrange in alphabetical order

