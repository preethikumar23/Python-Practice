#You have two numbers, and your challenge is to write a program that performs both addition and subtraction with them. However, if any subtraction results in a negative number, display it as a positive value. How will you tackle this and show the final results?
num1=float(input("Enter a number:"))
num2=float(input("Enter a number:"))

sum=num1+num2
sub=abs(num1-num2) #abs maintains the sub as positive

print("The sum is:", sum)
print("The sub is:", sub)