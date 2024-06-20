'''
consonents to lower
vowel to upper
in :
    placements
op:
    plAcEmEnts
'''
s="SchoOl"
n=""
for i in s:
    if i in "AEIOUaeiou":
        n+=i.upper()
    else:
        n+=i.lower()
print(n)