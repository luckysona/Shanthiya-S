s1,s2=input().split()
s1=str(s1)  
s2=int(s2)
L=[]   
for i in range(0,len(s1),s2):
  L.append(s1[i:i+s2])
print(*L)
