from data import morse_code

def word_to_morse(string):
    morse = []
    for char in string.upper():
        if char in morse_code:
            morse.append(morse_code[char])
        else:
            morse.append('')
    return ' '.join(morse)

word = input("Enter a word or sentence: ")
morse_word = word_to_morse(word)
print(morse_word)