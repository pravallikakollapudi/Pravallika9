def add(num):
    s = 0
    for i in range(1,num):
        if i % 3 == 0 or i % 5 == 0:
            s=s+i
    return s
print(add(1000))
