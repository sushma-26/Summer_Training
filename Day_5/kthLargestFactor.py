''' kth largest factor 
'''
l=12
k=2
p=0
if k==1:
    print(l)
else:
    for i in range(l,0,-1):
        if l%i==0:
            k=k-1
        if k==0:
            p=i
            break
    print(p)