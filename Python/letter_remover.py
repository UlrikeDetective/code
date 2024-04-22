def vowel_remover(text):
    string = ""
    for l in text:
        if l.lower() not in "aeiou":
            string += l
    return string
print(vowel_remover("hello world! Something Somewhere Somehow"))

def special_character_remover(text):
    string = ""
    for l in text:
        if l not in "!$§%&/()=?#+-,;.:":
            string += l
    return string
print(special_character_remover("hello world! Something. Somewhere, Somehow: How many $ & § do you have?"))