'''
sent: this is sushma
is rearranged as sushma3 this1 is2 is given find correct sentence
'''
s="sushma3 this1 is2"
r=s.split(' ')
x=[0]*len(r)
for i in r:
    x[int(i[-1])-1]=i[:-1]
print(' '.join(x))