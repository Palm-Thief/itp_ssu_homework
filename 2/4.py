a, b = map(int, input().split())

if a - 1 <= 0:
    a = 2

print(f"{'x':<5} {'y':<30}")

if a <= b:
    for x in range(a, b+1):
        y = (3.0**x - x**2) / ((-1)**x * (x - 1)**0.5)
        print(f"{x:<5} {y:<30.20f}")