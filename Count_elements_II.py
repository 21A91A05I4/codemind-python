n,m=map(int,input().split())
ls=list(map(int,input().split()))
lst=list(map(int,input().split()))
c=ls+lst
c=set(c)
d=0
for i in c:
    if i in ls and i not in lst:
        d+=1
for j in c:
    if j in lst and j not in ls:
        d+=1
print(d)