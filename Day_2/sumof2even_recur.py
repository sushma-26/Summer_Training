'''
add all even in a list
add all odd in a list
'''
def sum1(x,se,so):
    if x==len(a):
        '''r=[]
        r.append(se)
        r.append(so)
        return r'''
        return se,so
    if a[x]%2==0:
        se+=a[x]
    if b[x]%2==1:
        so+=a[x]
    return sum1(x+1,se,so)
a=list(map(int,input().split(',')))
b=list(map(int,input().split(',')))
#a=[5,2,4,3]
#b=[5,5,2,3]
print(sum1(0,0,0))