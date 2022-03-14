#Reading and Creating the dataset as a list of list
from csv import reader
file=open("finds.csv", 'r')
data=reader(file)

#The initial value of hypothesis
H=None
n=0

#This loop generalizes the specific hypothesis
#for all and only positive instances
for row in data:
    if row[-1]=='Yes':
        if H==None:
            H=row
        else:
            for i in range(len(row)-1):
                if H[i]!=row[i]:
                    H[i]='?'

#Maxymal Hypothesis:
print("Maxymal Hypothesis:", H[:-1])