'''
given string of m and f find m===f or m>f if m<f
'''
s=input()
c=0
for i in s:
    if c=='M':
        c+=1
    else:
        c-=1
if c==0:
    print('equal')
elif c<0:
    print('f')
else:
    print('m')

