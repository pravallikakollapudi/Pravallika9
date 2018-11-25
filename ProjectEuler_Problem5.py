def divisor(num):
    c=0
    for j in range(1250,num,2):
        c=0
        for i in range(1,21):
            if(num%i==0):
                c=c+1
        if c==20:
            return num
print(divisor(100000000))
