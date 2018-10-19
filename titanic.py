import pandas as pd
import numpy as np
titanic = pd.read_csv('http://biostat.mc.vanderbilt.edu/wiki/pub/Main/DataSets/titanic.txt')
titanic.head()
print ("1------------------")
titanic.info()
X = titanic[['pclass','age','sex']]
y = titanic['survived']
print ("2------------------")
X['age'].fillna(X['age'].mean(),inplace=True)
print ("3------------------")
X.info()
print ("4------------------")
from sklearn.cross_validation import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X, y, test_size=0.25, random_state=33)
X_train = X_train.to_dict(orient='record')
X_test = X_test.to_dict(orient='record')
print ("5------------------")
from sklearn.feature_extraction import DictVectorizer
from sklearn.tree import DecisionTreeClassifier
from sklearn.pipeline import Pipeline
clf = Pipeline([('vecd',DictVectorizer(sparse=False)),('dtc',DecisionTreeClassifier())])
vec = DictVectorizer(sparse=False)
print ("6------------------")
clf.fit(X_train,y_train)
y_predict = clf.predict(X_test)
from sklearn.metrics import classification_report
print (clf.score(X_test,y_test))
print ("7------------------")
print(classification_report(y_predict,y_test,target_names=['died','survivied']))
