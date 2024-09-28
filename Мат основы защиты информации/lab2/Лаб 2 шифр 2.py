def compress(key, val):  # similar for itertools.compress
    key = list(''.join(key))  # make all in one list like ['........']
    val = list(''.join(val))
    return ''.join(v for v, k in zip(val, key) if k == 'X')

def right_rotate(array):
    return tuple(map(lambda a: ''.join(reversed(a)),zip(*array)))

key = ( 'X...',
        '..X.',
        'X..X',
        '....')

value = ('itdf',
        'gdce',
        'aton',
        'qrdi')

(k,v) = (key, value)
l = ''
for i in range(4):
    l +=compress(k,v)
    k = right_rotate(k)

    print(l)