sum_before_neg = 0
cur_sum = 0
while (n := int(input())) != 0:
    if n > 0:
        cur_sum += n
    else:
        sum_before_neg += cur_sum
        cur_sum = 0

print(sum_before_neg if sum_before_neg != 0 else 'Вы обещали отрицательное!')
