from csv import reader
file=open("finds.csv", 'r')
data=reader(file)
rows=[]
for row in data:
    rows.append(row)
for _ in rows:
    print(_)