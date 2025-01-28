enter_the_string = input()
special_character = "!@#$%^&*()_+-=[]<>,.?/@"

updated_string = ""
for each_char in enter_the_string:
    if each_char in special_character:
        continue
    else:
        updated_string += each_char

print(updated_string)