def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            translation = translation + 'n'
        else:
            translation = translation + letter
    return translation


user_phr = input('Enter a phrase: ')

print(translate(user_phr))

# print(translate)