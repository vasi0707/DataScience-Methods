import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets, svm

iris = datasets.load_iris()
x = iris.data
y = iris.target

#x has 4 attributes, making it to only 2 attributes
#y has three classes [0,1,2], removing class 2

X = []
X0 = []
X1 = []
Y = []

for i in range(len(x)):
    if y[i]==2:
        continue
    else:
        Y.append(y[i])
        val = x[i]
        X.append(val[:2])
        if y[i]==0:
            X0.append(val[:2])
        else:
            X1.append(val[:2])

samples = len(X)

#Fitting using SVM

clf = svm.SVC(kernel='poly', gamma=10)
clf.fit(X,Y)

#Plotting the given data

plt.figure()
plt.clf()

plt1 = [*(zip(*X0))]
plt2 = [*(zip(*X1))]

plt.scatter(plt1[0],plt1[1],color='red')
plt.scatter(plt2[0],plt2[1],color='green')

#Finding the decision function

XX,YY = np.mgrid[2:8:200j,0:6:200j]
Z = clf.decision_function(np.c_[XX.ravel(),YY.ravel()])
Z = Z.reshape(XX.shape)

#Plotting the decision boundary

plt.contour(XX,YY,Z,colors=['blue','orange','blue'],linestyles=['--','-','--'],levels=[-0.5, 0, 0.5])
plt.title("SVM")

plt.show()

    
