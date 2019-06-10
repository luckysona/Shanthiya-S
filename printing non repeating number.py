x=int(input())  
y=list(map(int,input().split()))   
for i in y:
  if(y.count(i)==1):
    print(i)
