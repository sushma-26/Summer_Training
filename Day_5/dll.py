'''
we need object to use anything inside a class

var inside class can acessed outside with classname.var 
def asd():==static method without object
def asd(self):== non static method accessed with only object
'''
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
    def rev_display(self):
        t=self.tail
        print("reverse")
        while t:
            print(t.data,end='->')
            t=t.prev
        print()

    def search(self,x):
        t1=self.head
        t2=self.tail
        while t1!=t2 and t1!=t2.next:   #t1.prev.prev!=t2 for odd len
            if t1.data==x or x==t2.data:
                return 'yes'
            t1=t1.next
            t2=t2.prev
        if t1.data==x:
            return 'yes'
        else:
            return 'no'
    def evenorodd(self):
        t1=self.head
        t2=self.tail
        while t1!=t2 and t1!=t2.next:   
            t1=t1.next
            t2=t2.prev
        if t1==t2:
            return 'odd'
        else:
            return 'even'
    def palindrome(self):
        t1=self.head
        t2=self.tail
        while t1!=t2 and t1!=t2.next:
            if t1.data !=t2.data:
                return 'no'
            t1=t1.next
            t2=t2.prev
        return 'yes'
    def swapdata(self):
        t1=self.head
        t2=self.head
        while t2:
            t1=t1.next
            t2=t2.next.next
        s=self.head
        m=t1
        while m:
            s.data,m.data=m.data,s.data
            s=s.next
            m=m.next
    def changemiddlelink(self):
        t1=self.head
        t2=self.head
        while t2:
            t1=t1.next
            t2=t2.next.next
        self.head.prev=self.tail
        self.tail.next=self.head
        self.tail=t1.prev
        self.tail.next=None
        t1.prev=None
        self.head=t1
    '''5 7 8 2 1 4 == 7 5 2 8 4 1 '''
    def swaplinks2(self):
        a=self.head
        b=self.head.next
        c=None
        a.next=b.next
        b.prev=c
        b.next=a
        a.prev=b
        self.head=b
        a,b=b,a
        c=b
        while b and a:
            a.next=b.next
            b.prev=c
            b.next=a 
            a.prev=b
            c.next=b
            a,b=b,a
            c=b
            a=a.next.next
            b=b.next.next
    ''' ADD EVEN AND ODD NUMBERS AND RETURN DIFF B/W THEM'''
    def oddEvenDiff(self,t,o,e):
        if t==None:
            return abs(o-e)
        if t.data%2==0:
            e=e+t.data
        else:
            o+=t.data
        return self.oddEvenDiff(t.next,o,e)
    '''find sum of prime numbers using recursion with using recursion only find if its prime or not'''
    def prime(self,n,i):
        if n==2:
            return 1
        if i>((n)//2)+1:
            return 1
        if n%i==0:
            return 0
        return self.prime(n,i+1)

    def countPrime(self,t,c):
        if t==None:
            return c
        if self.prime(t.data,2)==1:
            c=c+1
        return self.countPrime(t.next,c)


x=dll()
x.addback(1)
x.addback(2)
x.addback(3)
x.addback(4)
x.addback(5)
x.addback(6)
x.display()
#x.rev_display()
#print(x.search(40))
#print(x.evenorodd())
#print(x.palindrome(),"it is a palindrome")
#x.swapdata()
#x.display()
#x.changemiddlelink()
#x.display()
#x.swaplinks2()
#x.display()
#print(x.oddEvenDiff(x.head,0,0))

print(x.countPrime(x.head,0))