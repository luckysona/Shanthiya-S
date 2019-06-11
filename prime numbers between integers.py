s1,s2=map(int,input().split())
s=0
for i in range(s1,s2+1):
    x=bin(i)
    x=x[2:len(x)]
    x=x.count("1")
    s2=0
    for i in range(1,x):
        if x%i==0:
            s2=s2+1
    if s2==1:
        s=s+1
print(s)
