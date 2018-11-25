def factorial(n):
    fact=1;
    for i in range(2,n+1):
        fact=fact*i
    x=sum_of_digits(fact)
    return x
def sum_of_digits(n):
    s=0
    while n > 0:
        r = n % 10
        s = s + r
        n = n // 10
    return s
print(factorial(100))
