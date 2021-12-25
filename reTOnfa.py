

#-------------------this code find or, dot or and operation only------------------------
print("Enter regular expression any input characters but only enter '+' or '.' character")
string=input()
str=""
star=''
for i in range(len(string)):
    if string[i]=='(' or string[i]==')':
        continue
    elif string[i]=='*':
        star='*'
    else:
        str+=string[i]

#print(str)
n=1
initial=1
final=2

nfa=[[]for i in range(50)]
nfa[n].append([str[0],n+1])
n+=2
temp=str[0]
for i in range(1,len(str)):
    if str[i]=='/' or str[i]=='+' or str[i]=='.':
        temp=str[i]
        continue
    if (temp=='+' or temp=='/') and str[i].isalpha():
        nfa[n].append([str[i],n+1])
        initial2=n
        final2=n+1
        n+=2
        nfa[n].append(['e',initial])
        nfa[n].append(['e',n-2])
        initial=n
        n+=1
        nfa[final].append(['e',n])
        nfa[final2].append(['e',n])
        final=n
        n+=1
    if (temp.isalpha() and str[i].isalpha()) or (temp=='.' and str[i].isalpha()):
        nfa[final].append(['e', n])
        nfa[n].append([str[i], n + 1])
        final = n + 1
        n += 2
    if star=='*':
        nfa[final].append(['e',initial])
        nfa[n].append(['e',initial])
        nfa[n].append(['e',n+1])
        nfa[final].append(['e',n+1])
        initial=n
        final=n+1
        n+=2

#print(nfa)



print("initial :",initial,"Final :",final)
print("state---------Input---------Next State")
for i in range(len(nfa)):
    if len(nfa[i])!=0:
        for j in nfa[i]:
            print("   ",i,"          ",j[0],"             ",j[1])






