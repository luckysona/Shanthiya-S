s1,s2=input().split()  
s1=str(s1)   
s2=str(s2)  
for i in s1:
  for j in s2:
    if(i==j):
      s=set(j)  
      print(*s,end="")
