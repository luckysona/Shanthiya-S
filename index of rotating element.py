N=input()  
N=int(N)   
s1=list(map(int,input().split()))
s2=list(map(int,input().split()))
for i in range(0,len(s1)):
  for j in range(0,len(s2)):
    i=s1.index(s1[N-2])
    j=s2.index(s1[i])
print(i-j) 
