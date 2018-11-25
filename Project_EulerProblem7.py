def isprime(num):
    k=0
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            k+=1
    if k==0:
        return True
    else:
        return False
c=0
l=[]
for i in range(2,200000):
    if isprime(i):
        l.append(i)
        c+=1
    if c==10001:
        break
print(l[-1])

                                                                                                                                                                     
