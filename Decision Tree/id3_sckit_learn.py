# import six
# import sys
# sys.modules['sklearn.externals.six']=six
# from id3 import ID3Estimator
# import pandas as pd

# estimator=ID3Estimator()
# estimator.fit(X,Y)
import pandas as pd
from sklearn.datasets import load_iris
from sklearn import tree
iris=load_iris()
file_data=pd.read_csv('train.csv')
X,Y=iris.data,iris.target
clf=tree.DecisionTreeClassifier()
clf=clf.fit(X,Y)
