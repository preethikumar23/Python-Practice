#You have a number to examine, and your mission is to write a program that checks  whether this number can be divided evenly by 27. Can you find out if it‟s a multiple of 27?

num=int(input("Enter a number:"))
if (num%27==0): #dividing the number by 27
    print("The number is divisible by 27")
else:
    print("The number is not divisible by 27")