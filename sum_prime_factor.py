l=[]
def sum_prime_factors(n):
    for i in range(2,int(n**(0.5))+1):
        if n%i==0:
            if prime(i):
                l.append(i)
    return l
def prime(n):
    c=0
    for i in range(1,int(n**(0.5))+1):

        if n%i == 0:
            c=c+1
    if c==1:
        return True
    else:
        return False
print(sum_prime_factors(100))

    

