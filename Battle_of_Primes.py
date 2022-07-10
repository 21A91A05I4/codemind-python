def isprime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return 0
    return 1

n=int(input())
m=int(input())
s=(n+m)
c=0
i=s+1
while s>0:
    if isprime(i)==1:
        c=i
        break
    i+=1
print(c-s)