# A Python program to print all  
# permutations of given length 

from itertools import permutations
S=input() 
perm = permutations(S) 
for i in perm: 
    print(*i)
