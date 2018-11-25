def palindrome(num):
    if(num == reverse(num)):
        return True
    else:
        return False
def reverse(num):
    rev=0
    while (num) >0:
        r=(num)%10
        rev=rev*10+r
        num=(num)/10
    return rev
l=[]
c=0
for i in range(100,1001):
    for j in range(100,1001):
        num=i*j
        if(palindrome(num)):
            l.append(num)
            c+=1
l=sorted(l)

print(l[-1])

