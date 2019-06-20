n=int(input())
s=list(map(int,input().split()))
L=[]
a=min(s)  
e=max(s)  
L.append(a)  
L.append(e)
print(*L)
