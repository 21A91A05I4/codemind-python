
n=int(input())
a=list(map(int,input().strip().split()))[:n]
c=0
for i in a:
    if(i!=0):
        print(i,end=' ')
    else:
        c+=1
for i in range(0,c):
    print(0,end=' ')
    


