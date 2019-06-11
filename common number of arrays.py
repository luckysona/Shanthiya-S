N,K=map(int,input().split())
g=[]
for i in range(N):
	s1=set(map(int,input().split()))
	g.append(s1)
a=s1.intersection(*g)
print(*a)
