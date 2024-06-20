#no of possible paths without touching obstacle
'''def count(a,b,i,j,k,l,c):
    if i==k-1 and j==l-1:
        c+=1
        return c
    #if i==a and j==b: #this condition wont be for all paths
        #return c
    if i<k-1:
        c=count(a,b,i+1,j,k,l,c)
    if j<l-1:
        c=count(a,b,i,j+1,k,l,c)
    return c
print(count(0,1,0,0,4,3,0))'''
def count(i,j,k,l,c,cl):
    #if i==a and i==b:   this condition for checking obstacle
    #    return c
    cl.append((i,j))
    if i==k-1 and j==l-1:
        for i,j in cl:
            print(l1[i][j],end="->")
        cl.pop()
        c+=1
        print()
        return c
    if i<k-1 and (i+1,j) not in cl:
        c=count(i+1,j,k,l,c,cl)
    if j<l-1 and (i,j+1) not in cl:
        c=count(i,j+1,k,l,c,cl)
    if i>0 and (i-1,j) not in cl:
        c=count(i-1,j,k,l,c,cl)
    if j>0 and (i,j-1) not in cl:
        c=count(i,j-1,k,l,c,cl)
    cl.pop()
    return c
l1=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print(count(0,0,3,4,0,[]))

