import string
import random

def text_func(text):
    ctext = ''
    for i in text:
        ctext_s = translation[i]
        ctext += ctext_s
    return(ctext)

translation = {}
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "
key = letters[::-1]
text = "BFKOALF"
random.seed(1)
k = 0
for i in letters:
    key_s = key[k]
    translation[i] = key_s
    k += 1


print("Текст:", text)
print("Ключ:", key)
ctext = text_func(text)
print('Зашифрованный текст:', ctext)