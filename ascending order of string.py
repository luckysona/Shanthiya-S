s=int(input())  
s1=[str(s) for s in input().split()]   
s1.sort()
for i in s1:
  print(i.lower())
