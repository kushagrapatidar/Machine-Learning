from csv import reader
file=open("finds.csv", 'r')
data=reader(file)
H=None
n=0
for row in data:
    if row[-1]=='Yes':
        if H==None:
            H=row
        else:
            for i in range(len(row)-1):
                if H[i]!=row[i]:
                    H[i]='?'
    print(f"Training Example number {n+1} hypothesis: ",H[:-1])
    n=n+1

print("\nMaxymal Hypothesis:", H[:-1])