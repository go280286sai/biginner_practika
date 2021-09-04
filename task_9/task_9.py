list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list_2 = [8, 5, 4, 3]


def my_fun(a, b):
    mas = []
    n = 0
    while n != len(a):
        if a[n] not in b:
            mas.append(a[n])
        n += 1
    return mas


print(my_fun(list_1, list_2))
