class node:
    data=None
    weights=list()
    next_attributes=dict()
    def _init_(self,head):
        self.data=head

def calculate_entropy(attribute):
    
    return 0
def calculate_gain(attribute,next_attribute):
    return 0
from csv import reader

from numpy import array
file=open("decisionTree.csv", 'r')
Data=reader(file)
Heads=None
for row in Data:
    if Heads==None:
        Heads=row
        break
Data=[row for row in Data]
Heads=Heads[:-1]
for _ in range(len(Heads)):
    temp=node()
    temp.data=Heads[_]
    Heads[_]=temp
for i in range(len(Heads)):
    Weights=[]
    for j in range(len(Data)):
        if Data[j][i] not in Weights:
            Weights.append(Data[j][i])
    Heads[i].weights=Weights
    for _ in Weights:
        if _ not in Heads[i].next_attributes.keys():
            Heads[i].next_attributes[_]=None
[print(Heads[_].next_attributes) for _ in range(len(Heads))]
# [print(row) for row in Data]