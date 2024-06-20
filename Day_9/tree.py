'''
hight of tree is height of root
height is from down count nodes to reach the number
depth from root count nodes to reach the number
'''
class node():
    def __init__(self,x) -> None:
        self.data=x
        self.left=None
        self.right=None
class tree:
    def __init__(self) -> None:
        self.root=None
    def create(self,root,x):
        if self.root is None:
            self.root = node(x)
            return self.root

        if root is None:
            return node(x)
        elif x < root.data:
            root.left = self.create(root.left, x)
        else:
            root.right = self.create(root.right, x)
        return root
    def inorder(self,root):
        if root:
            self.inorder(root.left)
            print(root.data,end="=>")
            self.inorder(root.right)
    def preorder(self,root):
        if root:
            print(root.data,end="=>")
            self.preorder(root.left)
            self.preorder(root.right)
    def postorder(self,root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data,end="=>")
    def sumOfNodes(self,root):
        if root==None:
            return 0
        if root.left == None and root.right==None: #optional no need 
            return root.data #optional no need 
        if root:
            return root.data+self.sumOfNodes(root.left)+self.sumOfNodes(root.right)
    def Addeven(self,root):
        if root==None:
            return 0
        if root.data%2==0:
            return root.data+self.Addeven(root.left)+self.Addeven(root.right)
        else:
            return self.Addeven(root.left)+self.Addeven(root.right)
        
    def diffOddEven(self,root):
        if root==None:
            return 0
        if root.data%2==0:
            return root.data+(self.diffOddEven(root.left)+self.diffOddEven(root.right))
        return -root.data+(self.diffOddEven(root.left)+self.diffOddEven(root.right))
    def height(self,root):
        if root==None:
            return -1
        return max(self.height(root.left),self.height(root.right))+1
#balanced subtree means if left subtree and right subtree is 1 or 0
    def balancedOrNot(self,root):
        if abs((self.height(root.right))-(self.height(root.left)))<=1:
            return True
        else:
            return False
    def sumOfleaf(self,root,c): 
        if root == None:
            return 0
        if root.left == None and root.right==None: 
            print(root.data,end="->")
            return root.data
        return self.sumOfleaf(root.right,c)+self.sumOfleaf(root.left,c)
    def countOfleaf(self,root): 
        if root == None:
            return 0
        if root.left == None and root.right==None: 
            return 1
        return self.countOfleaf(root.right)+self.countOfleaf(root.left)
    def searchandDepth(self,root,x,i):
        if root==None:
            return False
        if root.data==x:
            return i
        if root.data>x:
            return self.searchandDepth(root.left,x,i+1)
        else:
            return self.searchandDepth(root.right,x,i+1)
    def topViewR(self,root,c,d,n):
        if root==None:
            return 
        if c not in d or n<d[c][1]:
            d[c]=[root.data,n]
            #print(root.data,end="->")
        '''else:
            if d[c]<root.data:
                d[c]=root.data'''
        self.topViewR(root.left,c-1,d,n+1)
        self.topViewR(root.right,c+1,d,n+1)
    def topView(self,root):
        l=[]
        c=0
        d={}
        l.append((root,c))
        while l:
            node,i=l.pop(0)
            if i not in d:
                d[i] = node.data 
            if node.left:
                l.append((node.left,i-1))
            if node.right:
                l.append((node.right,i+1))
        for i in sorted(d):
            print(d[i],end="=>")
    def bottomView(self,root):
        l=[]
        c=0
        d={}
        l.append((root,c))
        while l:
            node,i=l.pop(0)
            d[i] = node.data 
            if node.left:
                l.append((node.left,i-1))
            if node.right:
                l.append((node.right,i+1))
        for i in sorted(d):
            print(d[i],end="=>")
    def verticalView(self,root):
        l=[]
        d={}
        l.append((root,0))
        while l:
            node,i=l.pop(0)
            d[i].append(node.data)
            if node.left:
                l.append((node.left,i-1))
            if node.right:
                l.append((node.right,i+1))
        for i in sorted(d):
            print(d[i],end="=>")
    



    def bottomViewR(self,root,c,d,n):
        if root==None:
            return None
        if c not in d or n>=d[c][1]:
            d[c]=[root.data,n]
        self.bottomViewR(root.left,c-1,d,n+1)
        self.bottomViewR(root.right,c+1,d,n+1)
    def leftView(self,root,l,c):
        if root==None:
            return
        if not l:
            l.append(c)
            print(root.data,end="=>")
        if c not in l:
            l.append(c)
            print(root.data,end="=>")
        self.leftView(root.left,l,c+1)
        self.leftView(root.right,l,c+1)
    '''def rightView(self,root,l,c): 199
        if root==None:
            return
        if c not in l:'''


d={}
t1=tree()
t1.create(t1.root,10)
t1.create(t1.root,5)
t1.create(t1.root,2)
t1.create(t1.root,7)
t1.create(t1.root,15)
t1.create(t1.root,11)
t1.create(t1.root,20)
t1.create(t1.root,4)
t1.create(t1.root,3)
t1.create(t1.root,12)
t1.create(t1.root,13)
t1.create(t1.root,14)
t1.create(t1.root,16)
#t1.inorder(t1.root)
#print()
t1.preorder(t1.root)
#print()
#t1.postorder(t1.root)
#print()
#print(t1.sumOfNodes(t1.root))
#print()
#print(t1.Addeven(t1.root))
#print()
#print(t1.diffOddEven(t1.root))
print()
#h=t1.height(t1.root)
#print(h)
#print(t1.balancedOrNot(t1.root))
#print(t1.countOfleaf(t1.root))
#print(t1.sumOfleaf(t1.root,0))
#print(t1.searchandDepth(t1.root,20,0))
#t1.topViewR(t1.root,0,d,0)
#for i in sorted(d):
#    print(d[i][0],end="=>")
#d={}
#print()
#t1.bottomViewR(t1.root,0,d,0)
#for i in sorted(d):
#    print(d[i][0],end="=>")

#t1.leftView(t1.root,[],0)
#t1.topView(t1.root)
#print()
#t1.bottomView(t1.root)
print()
t1.verticalView(t1.root)
