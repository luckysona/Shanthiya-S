N,K=map(int,input().split())
s=[int(x) for x in input().split()]
g=0   
for i in range(0,N):
  for j in range(i+1,N):
      f=s[i]+s[j]
      if(f==K):
        g=g+1
if(g>=1):
  print("YES")  
else:
  print("NO")
