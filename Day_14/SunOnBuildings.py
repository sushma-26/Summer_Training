l=[3,4,5,10,4,3]
m=l[0]
c=1
ll=len(l)
for i in range(ll):
    if m<l[i]:
        c+=1
        m=l[i]
print(c)
m=l[-1]
c=1
for i in range(ll-1,0,-1):
    if m<l[i]:
        c=c+1
        m=l[i]
print(c)