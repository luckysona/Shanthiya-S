str=input()
str=list(str)
for i in range(len(str)):
	if str[i]!=-1 :
		print(str[i],end="")
		a=str[i]
		for j in range(len(str)):
			if a==str[j] :
				str[j]=-1
