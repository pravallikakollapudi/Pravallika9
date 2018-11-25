first=1
second=1
result=2
while len(str(second))<1000:
    first,second=second,first+second
    result+=1
print(result)
