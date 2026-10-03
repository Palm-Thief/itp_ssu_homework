flag = False
suma = 0
while (n := int(input())) != 0:
    if n > 0:
        if flag:
            suma += n
    else:
        flag = True
print(suma)