import random
import time

# print(random.randrange(1, 100))
# print(random.randint(1, 99))
# numerosImprimidos = 0

# while numerosImprimidos < 6:
#     numerosImprimidos += 1
#     numeroRandom = random.randint(1, 61)

#     time.sleep(2)
#     print("Numero sorteado: ", numeroRandom)


pessoas = ["Maria", "Clara", "Rafael", "Ines", "Tenorio"]
sorteio = random.choice(pessoas)
print(sorteio)

# random.shuffle(pessoas)
# print(pessoas)

# sorteio = random.sample(pessoas, k=3)
# print(sorteio)

# mega = random.sample(range(1, 62), 6)
# print(mega)

print(f"{random.random():.2f}")