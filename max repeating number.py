r=int(input())
s=[int(i) for i in input().split()]
L=[]
d=0
for i in range(0,len(s)):
    if s.count(s[i])>d:
      d=s.count(s[i])
      a=s[i]
print(a)
