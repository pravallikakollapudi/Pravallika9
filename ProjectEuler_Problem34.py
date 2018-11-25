def digits(n):
    s=0
    while n>0:
        r=n%10
        s=s+factorial(r)
        n=n//10
    return s
def factorial(n):
    fact=1
    for i in range(2,n+1):
        fact=fact*i
    return fact

def sum_factorial(n):
    s=0
    for i in range(10,n+1):
        if i==digits(i):
            s=s+i
    return s
print(sum_factorial(1000000))
#only two numbers 145 and 40585
