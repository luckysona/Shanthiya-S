s=input()
s1=0
for i in s:
  s1=int(i)+s1
if str(s1)==str(s1)[::-1]:
  print("YES")
else:
  print("NO")
