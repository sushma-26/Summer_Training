#l=[2,5,2,3,6,7,1,0,5,7]
l=[4,3,4,5,6,1,0,6,7]
n=len(l)

'''j=0
i=1
if l[j]<l[i]:
    j+=1
    i+=1
s=0
p=0
la=0
while i<n:
    if l[i]<l[j]:
        s+=l[i]
        i+=1
    elif l[i]>=l[i]:
        p+=l[j]*(i-(j+1))
        p=p-s
        la+=p
        s=0
        j=i
        i=i+1
if s!=0:
    

print(p)'''
i=0
j=n-1
a=[0]*n
b=[0]*n
a[0]=l[i]
b[j]=l[j]
i+=1
j-=1
while i<n:
    if a[i-1]<l[i]:
        a[i]=l[i]
    else:
        a[i]=a[i-1]
    if b[j+1]<l[j]:
        b[j]=l[j]
    else:
        b[j]=b[j+1]
    i+=1
    j-=1
s=0
for i in range(n):
    s+=min(a[i],b[i])-l[i]
print(s)



    

