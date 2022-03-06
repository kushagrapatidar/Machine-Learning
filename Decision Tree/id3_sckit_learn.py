from sklearn import tree
from sklearn.preprocessing import LabelEncoder
import pandas as pd

filename="train.csv"
dataset=pd.read_csv(filename)
Y=list(dataset.columns)
Y=Y[1:]
X=dataset[Y]
print(Y)
print(X)
le=LabelEncoder()
le.fit(Y)
for col in Y:
    le.fit(X[col].astype(str))
    le.transform(X[col].astype(str))
