'''
match even from one list and odd from another list and add them


for i in range(n):
    if i%2==0:
        for j in range(n):
            if j %2!=0:
                s=i+j
while i<=n:
    if i%2==0:
        while j<=n:
            if j %2!=0:
                s=i+j
            j+=1
    i+=1
    
''''''
def AddEvnOdd(l,o,e,i,j):
    if i>=len(e):
        return l
    if j>=n:
        return AddEvnOdd(l,o,e,i+1,0)
    if e[i]%2==0 and o[j]%2!=0:
            l.append(e[i]+o[j])
    return AddEvnOdd(l,o,e,i,j+1)
    
a=[6,3,2,9,4,7]
b=[8,7,5,3,6,9]
#add every even with every odd number in 2nd array and store in list
#[13, 11, 9, 15, 9, 7, 5, 11, 11, 9, 7, 13]
n=len(b)
print(AddEvnOdd([],b,a,0,0))

def AddEvnOdd(l,o,e,i,j,s):
    if i>=len(e):
        return l
    if j>=n:
        if s!=0:
            s+=e[i]
            l.append(s)
        return AddEvnOdd(l,o,e,i+1,0,0)
    if e[i]%2==0 and o[j]%2!=0:
        s+=o[j]
    return AddEvnOdd(l,o,e,i,j+1,s)
    
a=[6,3,2,9,4,7]
b=[0,1,1,1,0,1]
#add even +add all even 6+1+1+1+1=10
n=len(b)
print(AddEvnOdd([],b,a,0,0,0)) '''
def AddEvnOdd(l,o,e,i,j,s):
    if i>=len(e):
        return l
    if j>=n:
        if s!=0:
            l.append(s)
        return AddEvnOdd(l,o,e,i+1,0,0)
    if e[i]%2==0 and o[j]%2!=0:
        s+=e[i]+o[j]
    return AddEvnOdd(l,o,e,i,j+1,s)
    
a=[6,3,2,9,4,7]
b=[8,7,5,3,6,9]
#[13, 11, 9, 15, 9, 7, 5, 11, 11, 9, 7, 13] add all even num sums in this 13, 11, 9, 15,=48
n=len(b)
print(AddEvnOdd([],b,a,0,0,0))
