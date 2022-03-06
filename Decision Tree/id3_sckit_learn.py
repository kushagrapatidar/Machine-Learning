from sklearn import tree
from csv import reader

file=open("train.csv", 'r')
filedata=reader(file)
data=[]
for row in filedata:
    data.append(row)
    print(row)
num_attributes=len(data[0])-1