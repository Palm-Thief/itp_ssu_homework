suma = 0
count = 0
while (n := int(input())) != 0:
    if n > 0:
        suma += n
        count += 1
print(suma / count)
