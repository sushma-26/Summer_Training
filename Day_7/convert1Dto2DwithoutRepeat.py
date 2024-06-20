'''
2 3 1 3 4 3 2
[[2, 3, 1, 4], [3, 2], [3]]

r=[]
j=[]
for i in l:
    if i not in j:
        j.append(i)
r.append(j)
j=[]
for i in l:
    if i not in r[-1] and i not in j:
        j.append(i)
    else:
        r.append(j)
        j = []
        j.append(i)
if j:
    r.append(j)
print(r)

'''
l=list(map(int,input().split()))
m=[]
c=0
n=len(l)
while c!=n:  #O(n*repeated values)
    r=[]
    for i in range(n):
        if not str(l[i]).isalpha():
            if l[i] not in r:
                c=c+1
                r.append(l[i])
                l[i]='a'
    m.append(r)
print(m)

l=list(map(int,input().split()))
d={}
m=[]
c=0
for i in a:
    if i not in d:
        d[i]=0
    else:
        d[i]+=1
while c!=n:  #O(n*repeated values)
    r=[]
    for i in d:
        if d[i]!=0:
            d[i]-=1
            r.append(i)
    m.append(r)
print(m)


