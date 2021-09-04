import random
m = 0
for i in range(999):
    m += 1
    n = random.randrange(999)
    if n == 777:
        print(f"Число 777 было найдено за {m} попыток")
        break
    if m == 100:
        print(f"Заданное число 777 за {m} попыток не было найдено")
        break
