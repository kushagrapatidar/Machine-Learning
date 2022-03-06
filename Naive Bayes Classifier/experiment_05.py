class attribute_head:
    attributeHead=None
    attributes=dict()

from csv import reader
import pandas as pd
file="naiveBayesClassifier.csv"
dataset=pd.read_csv(file)
attributeHead_lst=[]
for col in dataset:
    column=dataset[col]
    print(type(column))
    att=None
    att=attribute_head()
    attributeHead_lst.append(att)
    att.attributeHead=col
    att.attributes.keys()=column.unique()
    #Convert Series to a List
    
print(attributeHead_lst[1])
    