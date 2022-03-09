# from sklearn import tree
# from sklearn.preprocessing import LabelEncoder
# import pandas as pd

# filename="train.csv"
# dataset=pd.read_csv(filename)
# Y=list(dataset.columns)
# Y=Y[1:]
# X=dataset[Y]
# print(Y)
# print(X)
# le=LabelEncoder()
# le.fit(Y)
# for col in Y:
#     le.fit(X[col].astype(str))
#     X[col]=le.transform(X[col].astype(str))

#Alternate method
# import numpy as np # linear algebra
# import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
# from sklearn.model_selection import train_test_split
# from sklearn.model_selection import cross_validate
# from sklearn.model_selection import KFold
# from sklearn.tree import DecisionTreeClassifier
# from sklearn.ensemble import RandomForestClassifier

# from sklearn import metrics

# import matplotlib.pyplot as plt
# from sklearn.tree import plot_tree


# df_train = pd.read_csv('train.csv')
# # print(df_train)print(df_train)

# event_rates=[]
# for col in df_train.columns:
#     if col !='Example':
#         event_rates.append(df_train.groupby(col).size())
# # [print(rates,end="\n\n") for rates in event_rates]

# var_columns=[c for c in df_train.columns if c not in ['Example','Category']]
# # print(var_columns)
# X=df_train.loc[:,var_columns]
# Y=df_train.loc[:,'Category']
# X_train,X_valid,Y_train,Y_valid=train_test_split(X,Y,test_size=0.54,random_state=42)
# # print(X_train,'\n\n',X_valid,'\n\n',Y_train,'\n\n',Y_valid)

# model_tree=DecisionTreeClassifier(max_leaf_nodes=6, class_weight='balanced')
# model_tree.fit(X_train,Y_train)