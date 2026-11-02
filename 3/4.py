from math import log

n, a, b, h, eps = list(map(float, input().split()))

quantity = int((b - a) / h + eps)

for i in range(quantity + 1):
    x = a + i * h
    arg_ln = x + 1
    if arg_ln > eps and abs(x) > eps:
        ln_res = log(x + 1)
        chlen = 1 / (6 * x)

        suma = chlen
        for j in range(2, int(n) + 1):
            chlen *= 1 / (2 * j * (2 * j + 1) * x)
            suma += chlen

        y = ln_res * suma
        print(f'{x:.6f}', f'{y:.6f}')
    else:
        print(f'{x:.6f}', 'undefined')
