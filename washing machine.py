weight = int(input("Enter weight:")) 
water_level = input("Enter water level") #get input from user

if weight < 0:              
    print("INVALID INPUT")  
elif weight > 7000:
    print("OVERLOADED")
elif weight == 0:
    print("Time Estimated: 0 minutes")
elif water_level == 'L':
    if 0 < weight <= 2000:
        print("Time Estimated: 25 minutes")
    else:
        print("INVALID INPUT")
elif water_level == 'M':
    if 2001 <= weight <= 4000:
        print("Time Estimated: 35 minutes")
    else:
        print("INVALID INPUT")
elif water_level == 'H':
    if weight > 4000:
        print("Time Estimated: 45 minutes")
    else:
        print("INVALID INPUT")
else:
    print("INVALID INPUT")