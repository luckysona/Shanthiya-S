g=int(input())  
b=list(input().split())  
b.sort(reverse=True)
if 0 not in b:
  print("".join(b))
else:
  print(0)
