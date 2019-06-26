list=list(map(str,input()))  
i=0
while(i < len(list)-1):
    if list[i] == list[i+1]:
        del list[i]
        
    else:
        i = i+1
list=list[::-1]
print("".join(list))
