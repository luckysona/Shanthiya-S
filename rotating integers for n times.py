N,D=input().split()  
N=int(N)
D=int(D)   
s=list(map(int,input().split()))
s= (s[len(s) - D:len(s)]  
                 + s[0:len(s) - D])
print(*s) 
