s1=int(input())
s2=[int(s1) for s1 in input().split()]
for i in s2:
  if(s2.count(i)==1):
    print(i)
