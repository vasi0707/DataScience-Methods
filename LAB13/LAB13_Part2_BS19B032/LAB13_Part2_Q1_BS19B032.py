import numpy as np
import math
import pandas as pd
import matplotlib.pyplot as plt
import random

def sigmoid(mat):
    ans = []
    for x in mat:
        ans.append(((math.e)**x)/((math.e)**x+ 1))
    return ans

def grad(hw,weights,var):
    diff = hw-y
    for i in range(len(weights)):
        p = 0
        for j in range(m):
            p += (1/m)*(diff[j])*var[i][j]
        weights[i] = weights[i] - alpha*p
        
    return weights

def steepest_gradient_descent(weights,var,y,m,n):
    Iterations = 100000
    count = 0

    while(count<=Iterations):
        h = np.matmul(np.transpose(weights),var)
        hw = sigmoid(h)
        weights = grad(hw,weights,var)
        count += 1
        
    return weights

def logistic_regression(x,y,n,m,alpha):
    weights = [1.0]*(n+1)
    weights = np.array(weights)
    var = [1]*m
    var = [*var,*x]
    var = np.array(var)
    var = var.reshape(n+1,m)
    ans = steepest_gradient_descent(weights,var,y,m,n)

    return ans

alpha = 0.01

file = pd.read_csv('points_new.csv')
df = pd.DataFrame(file)

train = df.sample(frac=0.7)
test = df.drop(train.index)

w1 = train['x']
w2 = train['y']
y = train['label']
y = np.array(y)


n = 2
m = len(w1)

x = np.array([*w1,*w2])

ans = logistic_regression(x,y,n,m,alpha)

print("The weights are:")
print(ans)

x_line = np.linspace(0,10,10)
x_line1 = np.linspace(0,10,10)
y_line = []

for i in x_line:
    val = (0.5 - ans[0] - (ans[1]*i))/(ans[2])
    y_line.append(val)

plt.scatter(w1,w2,c=y)
plt.plot(x_line,y_line,color = 'green')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Logistic Regression - Train Data')
plt.show()

x_test = test['x']
y_test = test['y']
test_label = test['label']
predict_label = []

x1 = []
y1 = []
labels = []
for i in x_test:
    x1.append(i)
for j in y_test:
    y1.append(j)
for k in test_label:
    labels.append(k)

for i in range(len(x1)):
    if((ans[0] + (ans[1]*x1[i]) + (ans[2]*y1[i])) >= 0.5):
        predict_label.append(1)
    else:
        predict_label.append(0)

plt.scatter(x_test,y_test,c=test_label)
plt.title('Test Data')
plt.show()

plt.scatter(x_test,y_test,c=predict_label)
plt.title("Predicted Data")
plt.show()

TP = 0
FP = 0
FN = 0
TN = 0

for i in range(len(labels)):
    if labels[i]==1:
        if predict_label[i]==1:
            TP += 1
        else:
            FN += 1
    else:
        if predict_label[i]==1:
            FP += 1
        else:
            TN += 1

print("")
print("True Positive: ",TP)
print("False Negative: ",FN)
print("False Positive: ",FP)
print("True Negative: ",TN)
print("")

precision = TP/(TP+FP)

print("Presicion: ",precision)
print("")

recall = TP/(TP+FN)

print("Recall: ",recall)
print("")

F1 = 2*(precision*recall)/(precision+recall)

print("F1 score: ",F1)
print("")

accuracy = (TP+TN)/(TP+FP+FN+TN)

print("Accuracy: ",accuracy)
