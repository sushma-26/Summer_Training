class Node:
    def __init__(self,data) -> None:
        self.prev=None
        self.data=data
        self.next=None
class dll:
    def __init__(self) -> None:
        self.head=None
        self.tail=None
    def addback(self,x):
        if(self.head==None):
            self.head=Node(x)
            self.tail=self.head
        else:
            t=Node(x)
            self.tail.next=t
            t.prev=self.tail
            self.tail=self.tail.next
    def addf(self,x):
        if(self.head==None):
            self.head=Node(x)
            self.tail=self.head
        else:
            t=Node(x)
            self.head.prev=t
            t.next=self.head
            self.head=self.head.prev
    def display(self):
        t=self.head
        while t:
            print(t.data,end='=>')
            t=t.next
        print()
    def balenced(self):
        s=[]
        n=0
        t=self.head
        while t:
            n=n+1
            if t.data =='[' or t.data =='{'or t.data =='(':
                s.append(t.data)
            elif not s:
                return n
            else:
                if t.data ==']' and s.pop()!='[':
                    return n
                elif t.data ==')' and s.pop()!='(':
                    return n
                elif t.data =='}' and s.pop()!='{':
                    return n
            t=t.next
        if not s:
            return -1
        else:
            return n
x=dll()
s="[{(]}]"
#s="([{}])({}"
for i in s:
    x.addback(i)
print(x.balenced())