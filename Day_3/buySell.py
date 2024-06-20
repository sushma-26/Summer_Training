l=list(map(int,input().split()))
mp=0
b=l[0]
n=len(l)
for i in range(1,n):
    if b>l[i]:
        b=l[i]
    if l[i]>b and l[i]-b>mp:
        mp=l[i]-b
print(mp)