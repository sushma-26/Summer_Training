'''
all possible 3 3 combinations in list
l=[12345]
=[123][124][125][234]...
'''
a=list(map(int,input().split()))
n=len(a)
r=[]
'''i,j,k=0,0,0
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            print(a[i],a[j],a[k])
    print()'''
'''def combo(n,i,s,r):
    if len(s)==3:
        r.append(s)
        s=[]
        return
    for i in range(n):
        s.append(a[i])
        return combo(n,i+1,s,r)
a=list(map(int,input().split()))
n=len(a)
r=[]
s=[]
print(combo(n,0,s,r))
'''
def comb(l,k):
    def fun(r,s):
        if len(r)==k:
            print(r)
            return
        for i in range(s,len(l)):
            fun(r+[l[i]],i+1)
        return
    fun([],0)
a=[1,2,3,4]
k=3
comb(a,k)



