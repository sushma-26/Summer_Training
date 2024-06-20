'''to link both the nodes we need store obj of the next Node
10|ob(b) 20|None
a           b 
a.nxt=b
'''
class Node:
    def __init__(self,data) -> None:
        self.data=data
        self.nxt=None
class ll:
    def __init__(self) -> None:
        self.head=None
    def addback(self,x): #doesnt send head just self and val
        if self.head==None:
            self.addfront(x)
        t=self.head
        while(t.nxt!=None):
            t=t.nxt
        t.nxt=Node(x)
    def addfront(self,x):
        t=Node(x)
        t.nxt=self.head
        self.head=t
    def display(self):
        t=self.head
        while(t!=None):
            print(t.data,end="->")
            t=t.nxt
        print()
    def addeven(self):
        t=self.head
        s=0
        while(t!=None):
            if (t.data)%2==0:
                s=s+t.data
            t=t.nxt
        print()
        print("sum",s)
    def search(self,x):
        t=self.head
        f=0
        while(t!=None):
            if t.data==x:
                print("found")
                f=1
                break
            t=t.nxt
        if f==0:
            print("not found")
    def middle(self):
        t1=self.head
        t=self.head
        while(t1 and t1.nxt!=None):
            t=t.nxt
            t1=t1.nxt.nxt
        return t.data
    def pairs(self):
        t=self.head
        while t!=None:
            t1=t.nxt
            while t1!=None:
                print(t.data,t1.data)
                t1=t1.nxt
            t=t.nxt
    def len(self):
        t1=self.head
        while(t1 and t1.nxt!=None):
            t1=t1.nxt.nxt
        if t1==None:
            return "even"
        else:
            return "odd"
    def longestsubstring(self):
        t=self.head
        c=1
        m=1
        while( t and t.nxt!=None):
            if t.data+1!=t.nxt.data:
                c=1
            else:
                c=c+1
                if c>m:
                    m=c
            t=t.nxt
        return m
    def bubblesort(self):
        i=self.head
        p=None
        while i.nxt !=None:
            f=0
            j=self.head
            while j.nxt!=p:
                if  j.data > j.nxt.data:
                    j.data,j.nxt.data=j.nxt.data,j.data
                    f=1
                j=j.nxt
            if f==0:
                break
            p=j
            i=i.nxt
    def rev(self):
        t2=self.head.nxt
        while t2:
            t2
    


            
           
l1=ll()
l1.head=Node(1)
l1.addfront(2)
l1.addback(3)
l1.addback(1)
l1.addback(3)
l1.addback(4)
l1.display()
#l1.addeven()
#l1.search(120)
#print("middle",l1.middle())
#l1.pairs()
#print(l1.len())
#print(l1.longestsubstring())
#l1.bubblesort()
l1.rev()
l1.display()
