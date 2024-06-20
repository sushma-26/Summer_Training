'''
ip:
    school
    3
    l 2 ===> hoolsc
    r 3 ===>oolsch
    l 1 ===>chools
now 1st letter hoc
is an anagram of school
3 len 
sch cho hoo ool yes becoz of cho
'''

''' not work
def anagrams(s, k):
    def fun(r, s, str, R):
        if len(r) == k:
            R.append(''.join(r))
            return
        for i in range(s, len(str)):
            fun(r + [str[i]], i + 1, str, R)
    R = []
    fun([], 0, s, R)
    return R
'''
s=input()
n=int(input())
x=''
for i in range(n):
    b=input()
    if b[0]=='l':
        x=x+s[int(b[2])]
    else:
        x=x+s[-int(b[2])]
x=list(x)
x.sort()
b=[]
for i in range(len(s)-n+1):
    t=list(s[i:n+i])
    t.sort()
    b.append(t)
for i in b:
    if x == i:
        print("yes")
        break
else:
    print("no")
'''
for i in range(n):
    operation = input().split()
    d = operation[0]
    p = int(operation[1])
    a.append((d, p))
r=''
for i in a:
    x=''
    d,p=i
    if d=='l':
        n=p
        x=s[p:]+s[:p]
        r+=x[0]
    else:
        n=p
        x=s[-p:]+s[:-p]
        r+=x[0]
'''



