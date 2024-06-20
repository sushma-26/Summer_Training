'''
ip: 5
    01001
    10011
    00000
    10000
    10001
    how many ialands are there if 1's connected
'''
def count(i,j):
    if m[i][j]==1:
        m[i][j]=0
    else:
        return
    if i+1<n:
        count(i+1,j)
    if i-1>0:
        count(i-1,j)
    if j+1<n:
        count(i,j+1)
    if j-1>0:
        count(i,j-1)
def area(i,j,a):
    if m[i][j]==1:
        a=a+1
        m[i][j]=0
    else:
        return a
    if i+1<n:
        a=area(i+1,j,a)
    if i-1>0:
        a=area(i-1,j,a)
    if j+1<n:
        a=area(i,j+1,a)
    if j-1>0:
        a=area(i,j-1,a)
    return a

m=[[0,1,0,0,1],[1,0,0,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,0,0,0,1]]
n=5
s=0
'''for i in range(n):
    for j in range(n):
        if m[i][j]==1:
            s+=1
            count(i,j)
            
print(s)'''
a=0
for i in range(n):
    for j in range(n):
        if m[i][j]==1:
            r=area(i,j,0)
            if r>a:
                a=r
print(a)

            