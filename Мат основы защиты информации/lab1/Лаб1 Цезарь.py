import string
import random

def text_func(text):
    ctext = ''
    for i in text:
        ctext_s = translation[i]
        ctext += ctext_s
    return(ctext)
key = ""
translation = {}
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
text = "LNFKSLD"
random.seed(23)
for i in letters:
    key_s = random.choice(string.ascii_letters)
    translation[i] = key_s
    key += key_s


print("Текст:", text)
print("Ключ:", key)
ctext = text_func(text)
print('Зашифрованный текст:', ctext)