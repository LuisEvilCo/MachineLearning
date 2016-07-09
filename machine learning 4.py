from sklearn import tree
#Training data
'''
(f)         (f)
Part        NTE     label
--------------------------------------
LA4140      1465    IC
LA4170      1477    IC
LA4175      1481    IC
LA4185      1637    IC
LA4185T     1637    IC
LA4185TM    1637    IC    
LA4192      1667    IC
LA4192S     1667    IC     
LA4201      1470    IC
LA4260      1685    IC
LA4261      1685    IC
LA4270      1798    IC <--- train until here
LA4422      1388    IC
LA4440      1377    IC
LA4440-R    1377    IC
LA440R      1377    IC
LA4445      1707    IC
LA4460      1390    IC
LA4261      1685    IC
LA4270      1798    IC
'''

def translate ( value ):
    print value, #the ',' stops the jump of the line in python
    if value == 0:
        print "IC: integrated circuit\n"
    elif value == 1:
        print "T-PNP oscillator\n" 
    return

# features = [[ 0 = LA | 1 = T-PNP , part]]
#labels = 0 = IC | 1 = other #
features = [[0, 4140]]
labels = [0]#
features.append([0, 4175])
labels.append(0)#
features.append([0, 4170])
labels.append(0)#
features.append([0, 4175])
labels.append(0)#
features.append([0, 4185])
labels.append(0)#
features.append([0, 4192])
labels.append(0)#
features.append([0, 4201])
labels.append(0)#
features.append([0, 4260])
labels.append(0)#
features.append([0, 4261])
labels.append(0)#
features.append([0, 4270])
labels.append(0)#


features.append([1, 27]) 
labels.append(1)#

#create DecisionTree
clf = tree.DecisionTreeClassifier()
#train
clf = clf.fit(features, labels)
#test
translate( clf.predict([[0, 4422]]) )
translate( clf.predict([[0, 4440]]) )
translate( clf.predict([[0, 4445]]) )
translate( clf.predict([[0, 4460]]) )
translate( clf.predict([[1, 27]]))
translate( clf.predict([[1, 28]]))
translate( clf.predict([[1, 31]]))