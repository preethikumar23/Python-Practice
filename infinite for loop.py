num = 1
for _ in iter(int, 1):
    print(num)  
    num += 1
    if num > 8:  # Reset to 1 after 8
        num = 1