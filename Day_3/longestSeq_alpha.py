'''
longest seq of alphabets in string
in xyzabcdklmnopq
ot:7
'''
n=input()
m=len(n)
c=1
ma=1
for i in range(m-1):
    '''if i==(m-2) and (ord(n[i])+1)==ord(n[i+1]):
        c=c+2
        if c > ma:
            ma=c
    el'''
    if (ord(n[i])+1)==ord(n[i+1]):
        c=c+1
        if c > ma:
            ma=c
    else:
        c=1
    
print(ma)