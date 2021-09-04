my_list = ['один', 'два', 'три', 'четыре', 'пять',
           'шесть', 'семь', 'восемь', 'девять', 'десять']
n = int(input())


def my_fun(a, b):
    if len(a) / n >= 1:
        k = len(a) // b
        lq = len(a) % b
        if lq > 0 and lq <= k:
            lq = lq + 1
        elif lq > 0:
            lq = lq + 1
        mas = []
        total = ''
        m = 0
        s = k
        while k <= len(a) - lq:
            for i in range(m, k):
                total += a[i] + ' '
            total = total.rstrip()
            mas.append(total)
            m = m + s
            k += s
            total = ''
        if lq > 0:
            for i in range(m, len(a)):
                total += a[i] + ' '
            total = total.rstrip()
            mas.append(total)
        return mas
    else:
        return 0


print(my_fun(my_list, n))
