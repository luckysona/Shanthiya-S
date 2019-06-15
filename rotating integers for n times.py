N,D=input().split()  
N=int(N)
D=int(D)   
s=list(map(int,input().split()))
s= (s[D:] + s[:D]) 
  
print(*s) 
