from sklearn import tree

#Training data
'''
   horsepower     seats    label
   -----------------------------
   300            2        sports-car
   450            2        sports-car
   200            8        minivan
   150            9        minivan
'''

def translate ( value ):
	print value
	if value == 1:
		print "Sports-Car"
	elif value == 0:
		print "Mini-Van"
	return

#[horsepower, seats]
features = [[300, 2], [450, 2], [200, 8], [150, 9]]
#1 = sports-car, 0 = minivan
labels = [1, 1, 0, 0]
#create DecisionTree
clf = tree.DecisionTreeClassifier()
#train
clf = clf.fit(features,labels)
#900 horsepower, 1 seat = sportscar
translate( clf.predict( [[900, 1]]) )
#80 horsepower, 10 seats = mini-van
translate( clf.predict( [[80,10]]) )