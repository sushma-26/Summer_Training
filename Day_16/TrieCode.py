#word search and auto correct and listing in google search
class node:
    def __init__(self) -> None:
        self.d={}
        self.flag=0
class tries:
    def __init__(self) -> None:
        self.root=node()
    def insert(self,str):
        t=self.root
        for i in str:
            if i not in t.d:
                t.d[i]=node()
            t=t.d[i]
        t.flag=1
    def search(self,str):
        t=self.root
        for i in str:
            if i not in t.d:
                return False
            t=t.d[i]
        if t.flag==1:
            return True
    def prefixSearch(self,str):
        t=self.root
        for i in str:
            if i not in t.d:
                return False
            t=t.d[i]
        return True
    def allStrs(self,t,s,l):
        if t.flag==1:
            l.append(s)
            return l
        for i in t.d:
            l=self.allStrs(t.d[i],s+i,l) 
        return l
    def allStrsWithPrefix(self,str,s):
        t=self.root
        le=len(str)
        for i in range(le-1):
            if str[i] in t.d:
                s+=str[i]
                t=t.d[str[i]]
            else:
                return 0
        for i in t.d:
            return self.allStrs(t.d[i],s+i,[])
    def findmaxl(self,t,s,l,m):
        if t.flag==1:
            if len(s)>=m:
                if len(s)==m:
                    m=len(s)
                    l.append(s)
                else:
                    l=[]
                    m=len(s)
                    l.append(s)
            return l
        for i in t.d:
            l=self.findmaxl(t.d[i],s+i,l,m) 
        return l[0].sort
    def longestPrefixStr(self,str,s):
        t=self.root
        le=len(str)
        for i in range(le-1):
            if str[i] in t.d:
                s+=str[i]
                t=t.d[str[i]]
            else:
                return ""
        for i in t.d:
            return self.findmaxl(t.d[i],s+i,[],0)

            
t=tries()
t.insert("world")
t.insert("wood")
t.insert("won")
t.insert("apple")
#print(t.search("wood"))
#print(t.prefixSearch("wo"))

print(t.allStrsWithPrefix("wo",""))
l=["oe","wo","ap"]
m=0
st=""
k=[]
for i in l:
    s=t.longestPrefixStr(i,"")
    if m<len(s):
        m=len(s)
        st=s
        k=[]
        k.append(st)
    if m==len(s):
        m=len(s)
        k.append(s)
        k.sort()
        st=k[0]
print(st)