s1=input().split()
s2=[]
for i in s1:
  s2.append(i[::-1])
print(*s2)
