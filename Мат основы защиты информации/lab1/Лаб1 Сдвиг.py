import string
import random

def text_func(text):
    ctext = ''
    for i in text:
        ctext_s = 234 - ord(i)
        ctext += chr(ctext_s)
    return(ctext)
text ='ABCDFG'

print("Текст:", text)
ctext = text_func(text)
print('Зашифрованный текст:', ctext)