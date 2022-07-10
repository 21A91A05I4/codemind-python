def isprime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return 0
    return 1
def ispalin(n):
    rev=0
    t=n
    while(n>0):
        d=n%10
        rev=rev*10+d
        n=n//10
    if rev==t:
        return 1
    else:
        return 0
    
n=int(input())
c=0
i=n+1
while n>0:
    if isprime(i)==1 and ispalin(i)==1:
        c=i
        break
    i+=1
print(c)