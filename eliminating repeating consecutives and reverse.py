s1=input()
s2=''
for i in s1:
    if i not in s2:
        s2+=i 
print(s2[::-1])
