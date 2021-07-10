import random, string

tamanho = 16
chars = string.ascii_letters + string.digits + 'ç!@#$%&*+-'
random = random.SystemRandom()

print(''.join(random.choice(chars) for i in range(tamanho)))