import random

lavoro = random.randint(1, 5)
studio = random.randint(1, 5)
fortuna = random.randint(1, 5)
amore = random.randint(1, 5)
generale = (lavoro + studio + fortuna + amore) / 4

print(f"Lavoro: {lavoro}")
print(f"Studio: {studio}")
print(f"Fortuna: {fortuna}")
print(f"Amore: {amore}")
print(f"Generale: {generale}")