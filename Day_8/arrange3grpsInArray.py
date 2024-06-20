
a=[4,9,8,2,14,3,5,6]
n=len(a)
for i in range(n-2):
    if a[i]>a[i+1]:
        a[i],a[i+1]=a[i+1],a[i]
    if a[i+1] > a[i+2]:
        a[i+1],a[i+2]=a[i+2],a[i+1]
        if a[i]>a[i+1]:
            a[i],a[i+1]=a[i+1],a[i]
print(a)