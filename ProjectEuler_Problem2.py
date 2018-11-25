def fibo(num):
    ft=1
    st=2
    s=2
    for i in range(st,num+1):
        tt=ft+st
        ft=st
        st=tt
        if tt>4000000:
            break
        elif tt%2==0:
            s=s+tt
    return s
print(fibo(1000))
