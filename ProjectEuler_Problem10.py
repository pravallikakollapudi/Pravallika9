def prime(num):
    s=0
    for i in range(2,num):
        if isprime(i)==True:
            s=s+i
    return s
def isprime(num):
    c=0
    for i in range(2,(num//2)+1):
        if num%i==0:
            c=c+1
    if c==0:
        return True
    else:
        return False

print(prime(13))
