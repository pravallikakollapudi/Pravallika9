def addition(num):
    s1=0
    s2=0
    for i in range(1,num+1):
        s1=s1+i
        s2=s2+(i*i)
    return (s1*s1)-s2
print(addition(100))
