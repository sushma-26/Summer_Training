'''
in:
    f46feLK9y56u#@&56hIjbn6KJhA
op:
    lowervowels-2
    uppervowel-2
    lowerconson-
    uc
    digits
    special chars
'''
a="OAAOf46feLK9y56u#@&56hIjbn6KJhALL"
lv,uv,lc,uc,d,s=0,0,0,0,0,0
for i in a:
    if i.islower():
        if i in 'aeiou':
            lv+=1
        else:
            lc+=1
    if i.isupper():
        if i in 'AEIOU':
            uv+=1
        else:
            uc+=1  
    elif i.isdigit():
        d+=1
    elif(not i.isalnum()):
        s+=1
print("lv,uv,lc,uc,d,s")
print(lv,uv,lc,uc,d,s)
    