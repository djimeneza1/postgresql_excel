import random
s=input().strip()

t=''
for i in range(len(s)):
    t+=random.choice(s)

pos=random.randint(0,len(t))

randomletter=random.choice('abcdefghijklmnopqrstuvwxyz')

t=t[:pos]+randomletter+t[pos:]

print(t)

for i in t:
    if i not in s:
        print(i)

def findtheDifference(s:str,t:str)->str:
    result=''
    