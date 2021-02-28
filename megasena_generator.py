import random

dezenas = []

for i in range(1, 7):
  dezenas.append(random.randrange(1, 61))
  if dezenas.count(dezenas[-1]) > 1:
    dezenas.pop()
    dezenas.append(random.randrange(1, 61))
    i -= 1
dezenas.sort()
dezenas = list(map(str, dezenas))

print(f"MEGA SENA: {', '.join(dezenas)}.")
