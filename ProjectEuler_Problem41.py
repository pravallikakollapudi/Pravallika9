large=0
def pandigital_prime():
    n=7654321
    while not(ispandigital(str(n),7) and prime(n)):
        n=n-2
    return n
def prime(n):
    for i in range(2,int(n**(0.5))+1):
        c=0
        if n%i == 0:
            c=c+1
    if c==1:
        return True
    else:
        return False
def ispandigital(string,n):
    digits=len(string)
    if digits!=7:
        return False
    for i in range(1,digits+1):
        if str(i) not in string:
            return False
    return True
print(pandigital_prime())


