'''in:5
ou: 
    *****
    *123*
    *456*
    *789*
    *****'''
'''n=int(input())
k=1
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==n-1 or j==n-1:
            print('*',end='')
        else:
            print(k,end='')
            k+=1
    print()'''
'''
in=5
out: 
    ----a----
    ---aba---
    --abcba--
    -abcdcba-

n=int(input())
s=''
r=''
f=''
k=1
for i in range(n):
    print('-'*(n-i),end="")
    s=f+chr(ord('a')+i)+r
    r=f[::-1]
    f=f+chr(ord('a')+i)
    print(s,end="")
    print('-'*(n-i),end="")
    print()

in:4
ou :
    1111111
    1222221
    1233321
    1234321
    1233321
    1222221
    1111111
'''
n=int(input())
for i in range(n*2):
    for j in range(n*2):
        if i==0 or i==n-1 or j==0 or j==n-1:
            