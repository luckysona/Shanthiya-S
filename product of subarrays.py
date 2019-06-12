s1=int(input())
s2=list(map(int,input().split()))
r1=0
r2=1
for i in range(s1-1):
    for j in range(i+1,s1):
        r2=1
        k=s2[i:j+1]
        for o in k:
            r2*=o
        if r2>r1:
            r1=r2
        
print(r1)
