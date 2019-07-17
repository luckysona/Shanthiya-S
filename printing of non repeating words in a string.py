s1=input() 
L=[]
for i in s1:
  if s1.count(i)==1:
    L.append(i)  
    print(i,end="")
