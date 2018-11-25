def power_digit_sum():
    i=pow(2,1000)
    s=0
    while i>0:
        s = s + i % 10
        i = i // 10
    return s
print(power_digit_sum())
