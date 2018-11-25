def sum():
    c=0
    s=0
    for i in range(2,2000000):
        c=0
        for j in range(1,int((i**0.5))+1):
            if i%j==0:
                c=c+1
        if c==1:
            s=s+i
    return s
print(sum())
#execution takes time
