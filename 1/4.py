sum_before_last_neg = 0
count_before_last_neg = 0
cur_sum = 0
cur_count = 0
while (n := int(input())) != 0:
    if n > 0:
        cur_sum += n
        cur_count += 1
    else:
        sum_before_last_neg += cur_sum
        count_before_last_neg += cur_count
        cur_sum, cur_count = 0, 0

print(sum_before_last_neg / count_before_last_neg if
      sum_before_last_neg != 0 else 'Вы обещали отрицательное!')
