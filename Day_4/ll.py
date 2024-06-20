class Node:
    def  __init__(self,data=None,next=None):
        self.data=data
        self.next=next
class LL:
    def __init__(self) -> None:
        self.head=None
    def add_at_begin(self,data):
        node=Node(data,self.head)
        self.head==node
    def add_at_end(self,data):
        if self.head==None:
            node=Node(data,self.head)
            self.head==node
        t=self.head
        while t.next:
            t=t.next
        t.next=Node(data,self.head)
    def insert_at(self,data,p):
        if p==0:
            add_at_begin(data)
        if index<0 or index>self.get_length():
            raise Exception("Invalid Index")
        c=0
        t=self.head
        while t:
            if c == i - 1:
                node = Node(data, t.next)
                t.next = node
                break
            t=t.next
            c=c+1
        
