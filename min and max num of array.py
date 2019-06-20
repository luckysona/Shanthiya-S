n=int(input())
s=list(map(int,input().split()))
L=[]
a1=(s.index(min(s))+1)
e1=(s.index(max(s))+1)  
L.append(a1)  
L.append(e1)
print(*L)
