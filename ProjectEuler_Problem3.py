def prime(num):
    list=[]
    for i in range(2,num+1):
        if num % i == 0:
            if isprime(i):
                list.append(i)
    return list

def isprime(num):
    c=0
    for i in range(2,(num//2)+1):
        if num%i==0:
            c=c+1
    if c==0:
        return True
    else:
        return False

print(prime(1003333))
