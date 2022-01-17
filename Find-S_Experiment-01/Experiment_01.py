from csv import reader
file=open("Find-S_Experiment-01/finds.csv", 'r')
data=reader(file)
H=None
for row in data:
    if row[-1]=='Yes':
        if H==None:
            H=row
        else:
            for i in range(len(row)-1):
                if H[i]!=row[i]:
                    H[i]='?'
    else:
        continue

print(H[:-1])