'''
in:
    6
    011101
    010100
    101100
    000111
    110001
    111010
    loc:4 6
    1=====Tree 0 bare lands
op: how many remained without fire 8 
'''
def rec(i,j,n,r):
    if r[i][j]==0:
        return
    r[i][j]=0
    if i > 0:
        rec(i-1,j,n,r)
    if j > 0:
        rec(i,j-1,n,r)
    if i<n-1:
        rec(i+1,j,n,r)
    if j<n-1:
        rec(i,j+1,n,r)
r=[[0,1,1,1,0,1],[0,1,0,1,0,0],[1,0,1,1,0,0],[0,0,0,1,1,1],[1,1,0,0,0,1],[1,1,1,0,1,0]]
k=0
n=6
a=int(input())
b=int(input())
rec(a,b,n,r)
for i in range(n):
    for j in range(n):
        if r[i][j]==1:
            k=k+1
print(k)
