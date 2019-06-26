s1,s2=input().split()  
s1=int(s1)  
s2=int(s2)
s=list(map(int,input().split())) 
if (s1>0):  
  s=sorted(s)  
print(*s)
