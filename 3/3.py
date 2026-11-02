n, x = list(map(float, input().split()))

pow5 = 1
pow3 = 3
powx = x

res = 1
for i in range(1, n + 1):
    if i > 1:
        pow5 *= 25
        pow3 *= 9
        powx *= x
    numerator = (pow5 - pow3) * x
    denominator = (2*i) ** 0.5
    res *= numerator / denominator

print(res)
