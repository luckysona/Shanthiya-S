s1,s2=map(int,input().split())
count=0
for i in range(s1,s2+1):
  if(i%2!=0):
    count=count+1
print(count+1)
