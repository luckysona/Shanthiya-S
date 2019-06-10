x=int(input())
y = [int(y) for y in input().split()]
for i in range(0,x):
    if i<x-1:
        b=' '
    else:
        b=''
    if i%2==0:
        if y[i]%2!=0:
            print(y[i],end=b)
    elif i%2!=0:
        if y[i]%2==0:
            print(y[i],end=b)
