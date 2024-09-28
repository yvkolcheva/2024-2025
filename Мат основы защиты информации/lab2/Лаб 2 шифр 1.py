import numpy as np
translation = {}
key = 'kdc'
text = "BFK_ALF"

matr0 = text.split(sep="_")
matr = []
for i in matr0:
    matr.append(list(i))
matr = np.array(matr)

j = 0
for i in key:
    translation[i] = str(matr[:,j])
    j+=1

answer = dict(sorted(translation.items()))
a = answer.values()
print('Текст: ', text)
print('Ключ: ',key)
print(*a)

