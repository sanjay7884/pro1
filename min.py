from itertools import combinations
x,y=input().split()
y=int(y)
k=[]
c=len(x)-y
f=combinations(x,c)
for i in list(f):
  k.append("".join(i))
print(min(k))
