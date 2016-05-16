from sklearn import tree
from sklearn.datasets import load_iris
import numpy as np

def translate ( value ):
	for i in range ( len(value)):
		print i
		if i == 0:
			print"setosa"
		elif i == 1:
			print "versicolor"
		elif i == 2:
			print "virginica"

		
# https://en.wikipedia.org/wiki/Iris_flower_data_set#Data_set
iris = load_iris()
test_idx = [0,50,100]

'''
print iris.feature_names
print iris.target_names
print iris.data[0]
print iris.target[0]

for i in range ( len(iris.target) ):
	print "Example %d: label %s, features %s" % (i, iris.target[i], iris.data[i])

'''
#training data
train_target = np.delete(iris.target, test_idx)
train_data = np.delete(iris.data, test_idx, axis=0)

#testing data
test_target = iris.target[test_idx]
test_data = iris.data[test_idx]

#create tree && train
clf = tree.DecisionTreeClassifier()
clf.fit(train_data, train_target)

print test_target
print clf.predict(test_data)
translate(clf.predict(test_data))

### supertest

import pydot 

from sklearn.externals.six import StringIO
with open("iris.dot", 'w') as f:
     f = tree.export_graphviz(clf, out_file=f)
import os
os.unlink('iris.dot')

from IPython.display import Image  
dot_data = StringIO()  
tree.export_graphviz(clf, out_file=dot_data,  
                         feature_names=iris.feature_names,  
                         class_names=iris.target_names,  
                         filled=True, rounded=True,  
                         special_characters=True)  
graph = pydot.graph_from_dot_data(dot_data.getvalue())  
Image(graph.create_png())  