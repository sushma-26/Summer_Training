'''
each element should be present from each row
in:
    3
    xyz
    pqr
    abc
    "xpbzrbzr"
    out:true
 in:
    3
    xyz
    pqr
    abc
    "xpbzrbzb"
    out:false
    without reusing element which is used once
'''
'''f=True
n=int(input())
m = []
for i in range(n):
    a = []
    for j in range(n):
        value = input()
        a.append(value)
    m.append(a)
''''''for i in range(n):
    m.append(input())'''
'''s=input()
sl=len(s)
for i in range(sl):
    if s[i] in m[i%n]:
        m[i%n].remove(s[i])
    else:
        f=False
print(f)
'''
n=int(input())
m = []
for i in range(n):
    m.append(list(input()))  
str=input()
f=0
for i in range(len(str)):
    if(str[i] not in m[i%n]):
        print("no")
        f=1
        break
    else:
        m[i%n].remove(str[i])
if(f==0):
    print("yes")