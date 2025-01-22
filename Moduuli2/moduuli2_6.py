import random

# Kolmenumeroinen koodi (numerot 0..9)
kolmenumeroinen_koodi = ''.join(str(random.randint(0, 9)) for _ in range(3))

# Nelinumeroinen koodi (numerot 1..6)
nelinumerooinen_koodi = ''.join(str(random.randint(1, 6)) for _ in range(4))

# Tulostetaan molemmat koodit
print(f"Kolmenumeroinen koodi: {kolmenumeroinen_koodi}")
print(f"Nelinumeroinen koodi: {nelinumerooinen_koodi}")
