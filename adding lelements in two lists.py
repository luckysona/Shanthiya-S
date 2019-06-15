N=input()  
N=int(N)   
s1=list(map(int,input().split()))
s2=list(map(int,input().split()))
L=[]
for i in range(0,len(s1)):
  L.append(s1[i]+s2[i]) 
print(*L)
