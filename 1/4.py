sum_before_last_neg = 0
n_before_last_neg = 0
cur_sum = 0
cur_n = 0
while (n := int(input())) != 0:
    if n > 0:
        cur_sum += n
        cur_n += 1
    else:
        sum_before_last_neg += cur_sum
        n_before_last_neg += cur_n
        cur_sum, cur_n = 0, 0

print(sum_before_last_neg / n_before_last_neg if sum_before_last_neg != 0 else 'Вы обещали отрицательное!')
