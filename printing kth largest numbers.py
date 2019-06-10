N,K=map(int,input().split())
s1=list(map(int,input().split()))   
s1.sort(reverse=True)
print(s1[K-1])
