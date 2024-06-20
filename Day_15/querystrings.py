'''
ip:7            ip: 4
   1 school         1 car
   1 world          1 cap
   1 word           2 ca
   1 scholar        3 ca
   2 word           op:
   2 wood           False
   3 sch            true
op:
    true
    false
    true
   1 means insert word 2 means search for word if there print true if not print false
   3 means search for prefix
'''
nl=int(input())
l=[]
for i in range(nl):
    n,s=input().split(" ")
    if int(n)==1:
        l.append(s)
        print(l)
    elif int(n)==2:
        if s in l:
            print("true")
        else:
            print("false")
    elif int(n)==3:
        sl=len(s)
        c=0
        if not l:
            print("0")
        else:
            nl=len(l)
            for i in range(nl):
                s1=l[i]
                if s1[:sl]==s and s1 not in l[:i]:
                    c+=1
            print(c)
    elif int(n)==4:
        l.remove(s)
        print(l)
    
