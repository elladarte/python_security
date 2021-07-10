import itertools

resultado = itertools.permutations('abc', 3)

for i in resultado:
    print(''.join(i))
