'''s='abfgresagtyuiofde'
n=len(s)
m,c,i=0,0,0
r=''
while i<n:
    if s[i] not in r:
        r+=s[i]
        c=c+1
    else:
        r=''
        j=i-1
        while s[i]!=s[j]:
            j-=1
        i=j
        if c>m:
            m=c
        c=0
    i+=1
if c>m:
    m=c
print(m)'''

a='abfgresagtyauiofde'
d={}
s=""
m=0
n=len(a)
i=0
while i<n:
    if a[i] not in s:
        s+=a[i]
        d[a[i]]=i
    else:
        if len(s) > m:
            m=len(s)
        s=""
        i=d[a[i]]
    i+=1
print(m)


