'''
in:
    3 5 4 3 6 7 1 2 4 3 3 7 6
ot:
    3-4
    5-1
    4-2
    6-2
    7-2
    1-1
    2-1
d=[]
for i in l:
    if i in d:
        d.append(i)
for i in d:
    print(i,"=",l.count(i))
'''
l=list(map(int,input().split()))
d={}
for i in l:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
for key, value in d.items():  
    print(key, "-", value)