from sklearn import tree

#Training data
'''
   (feature)	(feature)
   weight		texture		label
   -------------------------------
   150g			bumpy		orange
   170g			bumpy		orange
   140g			smooth		apple
   130g			smooth		apple
'''
#change the result to a human form
def translate ( value ):
	print value
	if value == 1:
		print "Its an Orange !"
	elif value == 0:
		print "Its an Apple !"
	return

# 0 = bumpy, 1 = smooth
features = [[150, 0], [170, 0], [140, 1], [130, 1]]
# 0 = apple, 1 = orange
labels = [1, 1, 0, 0]
#create DecisionTree
clf = tree.DecisionTreeClassifier()
#train
clf = clf.fit(features, labels)
#150g && bumpy = orange, 1 = orange
translate( clf.predict([[150, 0]]) )
translate( clf.predict([[135, 1]]) )