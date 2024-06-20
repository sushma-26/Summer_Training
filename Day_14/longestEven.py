'''
ip:te5n2vn1ij8f
   vv5ojg8okg6og3o
   op:take unique numbers and print them as longest even num
     865312
'''
s="te5n2vn1ij8f"
s1="vv5ojg8okg6og3o"
n=[]
for i in s:
    if i.isdigit() and i not in n:
        n.append(i)
for i in s1:
    if i.isdigit() and i not in n:
        n.append(i)
n.sort(reverse=True)
last=0
for i in n[::-1]:
    if int(i)%2==0:
        last=i
        break
else:
    print(-1)
if last:
    n.remove(last)
    m=0
    for i in n:
        m=m*10+int(i)
    print(m*10+int(last))


