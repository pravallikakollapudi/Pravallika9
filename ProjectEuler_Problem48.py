def power(n):
    return pow(n,n)
def powersum(n):
    s=0
    for i in range(1,n+1):
        s=s+power(i);
    return s
print(powersum(1000))
