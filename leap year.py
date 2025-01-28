year=int(input("Enter a year:"))
if (year%4 & year%100 & year%400) == 0:
    print("It is a leap year")
else:
    print("Not a leap year")

