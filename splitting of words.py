s1,s2=input().split()
s1=str(s1)  
s2=int(s2)
L=[] 
for i in range(len(s1)-s2+1):
	L.append(s1[i:i+s2])  
print(*L)
