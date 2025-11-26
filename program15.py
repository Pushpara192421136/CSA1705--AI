from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt 
X = [[0,0],[0,1],[1,0],[1,1]]
y = [0,1,1,0]  
clf = DecisionTreeClassifier()
clf.fit(X, y)
print("Predictions:", clf.predict([[0,0],[1,1]]))
plt.figure(figsize=(4,4))
plot_tree(clf, filled=True)
plt.show()
