l=[]
a=pow(2,7830457)
s=(28433*a)+1
c=0
while s>0:
    c=c+1
    l.append(s%10)
    s=s//10
    if c==10:
        break
print(l)

