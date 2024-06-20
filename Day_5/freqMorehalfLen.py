'''
[4824484] find 
output should be freq of elem which is more than half of len
'''
a=list(map(int,input().split()))
p,c=a[0],1
for i in range(1,len(a)):
    if a[i]==p:
        c=c+1
    else:
        c=c-1
        if c==0:
            c=c+1
            p=a[i]

print(p)



