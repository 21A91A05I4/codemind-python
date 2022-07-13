n=int(input())
ls=list(map(int,input().split()))
for i in range(0,n):
    j=i
    if i%2!=0:
        while ls[i]>0:
            print(ls[j-1],end=' ')
            ls[i]-=1