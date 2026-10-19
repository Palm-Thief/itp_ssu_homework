a, b = map(int, input().split())

prev = 0
cur = 1
while cur <= b:
    if cur >= a:
        print(cur)
    prev, cur = cur, prev + cur
