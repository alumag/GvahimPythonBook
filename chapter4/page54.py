letters = "aeiou"

# in python3 raw_input renamed to input
# READ MORE: https://goo.gl/qBJjVp
phrase = input("Enter a sentence: ")

for letter in letters:
    if letter in phrase:
        # split the phrase, this function return the sliced phrase
        # without the letter, we will need to "add" it later.
        sliced_phrase = phrase.split(letter)
        # join function concat the separator ('b') between the sliced phrase
        # READ MORE: https://goo.gl/Ww2TGF
        phrase = (letter+'b'+letter).join(sliced_phrase)

print(phrase)
