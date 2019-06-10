s1=int(input())
s2=list(map(int,input().split()))
L=[]
for i in s2:
  if(s2.count(i)>1):
      L.append(i)
x=set(L)
if len(x)==0:
    print('unique')
else:
    print(*x) 
