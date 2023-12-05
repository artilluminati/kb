def count_vowels(word):

    vowels = "aeiou"

    return sum(1 for char in word if char.lower() in vowels)

word = "Python"

result = count_vowels(word)

print(result)