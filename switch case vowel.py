def remove_vowels(sentence):
    vowels = "aeiouAEIOU"
    switch = {
        "vowel": lambda char: char not in vowels
    }
    result = ''.join([char for char in sentence if switch["vowel"](char)])
    return result
sentence = input("Enter a sentence: ")
result = remove_vowels(sentence)
print("Sentence without vowels:", result)

