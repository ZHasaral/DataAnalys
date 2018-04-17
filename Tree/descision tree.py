from sklearn import tree
get = tree.DecisionTreeClassifier()


x= [[180,15,0],[167,42,1],[136,35,1],[174,15,0],[141,28,1]]
y=['man','woman','woman','man','woman']

get = get.fit(x,y)

result = get.predict([[input(),input(),input()]])
print(result)