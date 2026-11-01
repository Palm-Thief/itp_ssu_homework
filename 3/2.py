n = int(input())
pow_2 = 1
i = 0

suma = 0
while pow_2 <= n:
    for _ in range(pow_2 - i - 1):
        input()
    suma += int(input())
    i = pow_2
    pow_2 *= 2

print(suma)