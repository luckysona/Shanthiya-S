s1=int(input())
s2=0
for i in range(2,s1+1):
        while i>0:
            l=i%10
            if l==2:
                s2=s2+1 
            i=i//10
print(s2)
