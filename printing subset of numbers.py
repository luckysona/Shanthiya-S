N,K=map(int,input().split())
s1=list(map(int,input().split()))   
s2=list(map(int,input().split())) 
count=0
for i in range(0,len(s2)):
	if s2[i] in s1:
		count+=1
if count==len(s2):
	print("YES")
else:
	print("NO") 
