'''
remove nearest ele to *
'''
s="loo**pp*e*"
p=[]
for i in s:
    if i =='*'and p:
        p.pop()
    else:
        p.append(i)
print(''.join(p))