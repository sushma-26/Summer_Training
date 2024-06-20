'''
ip:
5 3.8 7 5.6 4 2 3
op:
e=15
o=6
float=9.4
'''
l=input().split()
e,o,f=0,0,0
for i in l:
    if i.isdigit():
        n=int(i)
        if n%2==0:
            e+=n
        else:
            o+=n
    elif '.' in i:
        n=float(i)
        f+=n
print("e,o,f",e,o,f)