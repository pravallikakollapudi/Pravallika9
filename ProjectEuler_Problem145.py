def total():
    count=0
    for i in range(1,1000000001):
        s=i+rev(i)
        if i%10!=0 and (rev(i))%10!=0:
                if isodd(s):
                    count=count+1
    return count
def rev(n):
    s=0
    while n>0:
        s=(s*10)+(n%10)
        n=n//10
    return s
def isodd(n):
    r=0
    while n>0:
        r=n%10
        if r%2==0:
            return False
        else:
            n=n//10
    return True
print(total())
# execution taking time
