s1=input()
s1=int(s1)
a1=[]
for i in range(0,s1):
    n=input()
    a1.append(n)
s=[]
for i in zip(*a1):
    if i.count(i[0])==len(i):
        s.append(i[0])
    else:
        break
print(''.join(s))
