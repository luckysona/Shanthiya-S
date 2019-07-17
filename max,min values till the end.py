s1=int(input())   
s2=list(map(int,input().split())) 
l=[]
f=True 
for i in range(s1):  
  if f:
    a=(max(s2))
    l.append(a)
    s2.remove(a)
    f=False
  else:  
    b=(min(s2)) 
    l.append(b)  
    s2.remove(b)
    f=True 
for i in l:   
  print(i,end=" ")  
