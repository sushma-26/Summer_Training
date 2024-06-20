'''def minimumspanningTree(d,i,l):
    l.append(i)
    #print(i)
    for i in d[i]:
        if i not in l:
            minimumspanningTree(d,i,l)
    return l'''
def findallPaths(i,l,j):
    l.append(i)
    if l and l[-1]==j: # or i==j
        print(l,end="=>")
    for i,j in d[i]:
        if i not in l:
            findallPaths(i,l,j)
    l.pop()
def weightForPath(i,l,j,s):
    l.append(i)
    if i==j: # or i==j
        print(l,"w=",s,end="=>") #list is dynamic doesnt change in recursion so change in program but values will change accordingly
    for i in d[i]:
        k,r=i[0],i[1]
        if k not in l:
            weightForPath(k,l,j,s+r)
    l.pop()
def minweightForPath(i,j,l,s,m,ml):
    l.append(i)
    if i==j :
        if m>s: # or i==j
            m=s
            ml=l.copy()
        l.pop()
        return m,ml
    for i in d[i]:
        k,r=i[0],i[1]
        if k not in l:
            m,ml=minweightForPath(k,j,l,s+r,m,ml) #should not return becoz it is not called by any recursive function so just give m value == returned value
    l.pop()
    return m,ml
def bfs(i,v,q):
    q.append(i)
    while q:
        for i in d[q[0]]:
            if i not in q and i not in v:
                q.append(i)
        v.append(q.pop(0))
    return v
def dijkstra(l,q): 
    v=[]
    n=5
    q.append(n)
    pa=float('inf')
    while q:
        pa=float('inf')
        for i in q:
            if l[i]<pa:
                n=i
                pa=l[i]
        for i,j in d[n]:
            if i not in v:
                q.append(i)
                if l[i]>j+l[n]:
                    l[i]=j+l[n]
        v.append(n)
        q.remove(n)

    print(l)
        

        

d={5:[(7,1),(3,2)],7:[(5,1),(4,3),(3,2)],4:[(7,3),(8,2),(2,1)],8:[(3,2),(4,2),(2,2)],3:[(5,2),(7,2),(8,2)],2:[(4,1),(8,2)]}
#d={2:[3,5],3:[2,6],5:[2,6],6:[3,5,7],7:[6,8],8:[7]}

i = list(d.keys())[0]
#print(minimumspanningTree(d,i,[]))
#for j in d.keys():
#  findallPaths(i,[],j)
#weightForPath(i,[],2,0)
print()
#print(bfs(i,[],[]))
#print(minweightForPath(i,2,[],0,1000000000,[]))
l={}
for k in d.keys():
    l[k]=float('inf')
l[i]=0
dijkstra(l,[])