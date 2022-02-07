class node:
    data=None
    weights=list()
    next_attributes=None
    def _init_(self,head):
        self.data=head

def calculate_entropy(attribute):
    
    return 0
def calculate_gain(attribute,next_attribute):
    return 0

from csv import reader
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
[print(Heads[_].data,": ",Heads[_].weights) for _ in range(len(Heads))]
# [print(row) for row in Data]
for x in range(len(Heads)):
    Heads[x].next_attributes=dict()
    for weight in Heads[x].weights:
        if weight not in Heads[x].next_attributes.keys():
            Heads[x].next_attributes[weight]=None
    print(Heads[x].data,Heads[x].next_attributes.keys())