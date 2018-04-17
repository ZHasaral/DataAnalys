from sklearn import tree
get = tree.DecisionTreeClassifier()
#подготовка = 0,1,2
#сложность(легкий, сложный) = 0,1
# не готов,готов= 0,1

x= [[1,1,0],[0,1,1],[2,1,0],[1,0,0],[1,0,1],[0,1,1],[2,0,1]]
y=['fail','pass','pass','pass','pass','fail','pass']

get = get.fit(x,y)

result = get.predict([[input("Введите уровень подготовки "),input("Введите сложность "),input("Подготовка к теме ")]])
print(result)