#Under Developement
from csv import reader
file=open("candidateelim.csv", 'r')
data=reader(file)
H=None
G=[]
n=0
for row in data:
    if row[-1]=='Yes':
        if H==None:
            H=row[:-1]
        else:
            for i in range(len(row)-1):
                if H[i]!=row[i]:
                    H[i]='?'
    elif H!=None and row[-1]=='No':
        for i in range(len(H)):
            h=['?']*len(H)
            if H[i]!=row[i]:
                h[i]=H[i]
            G.append(h)
    elif H==None and row[-1]=='No':
        for i in range(len(row[:-1])):
            h=['?']*len(row[:-1])
            h[i]=row[i]
            if h not in G:
                G.append(h)
        
    n=n+1
print(G)
for g in G:
    for i in range(len(g)):
        if H[i]==g[i]:
            continue
        else:
            g[i]='?'

while True:
    if ['?']*len(H) in G:
        G.remove(['?']*len(H))
    else:
        break

print(G)
print("\n\nMaxymal Hypothesis:", H)