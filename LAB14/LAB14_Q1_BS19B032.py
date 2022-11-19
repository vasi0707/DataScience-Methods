import numpy as np
import pandas as pd
import random
import matplotlib.pyplot as plt

def sigmoid(x):
    ans = 1/(1+np.exp(-x))
    return ans

def BP(z1,a1,z2,a2,X,Y,w1,w2):
    dZ2 = a2 - Y
    dW2 = (1/m)*np.matmul(dZ2,np.transpose(a1))
    dW2 = dW2.reshape(w2.shape)
    db2 = (1/m)*(np.sum(dZ2,axis=1,keepdims=True))
    dZ1 = a2 - Y
    dW1 = (1/m)*(np.matmul(a1,X))
    dW1 = dW1.reshape(w1.shape)
    db1 = (1/m)*(np.sum(dZ1,axis=1,keepdims=True))
    return dW1,dW2

def FP(w1,w2,X):
    z1 = np.dot(np.transpose(w1),np.transpose(X))
    a1 = sigmoid(z1)
    z2 = np.dot(np.transpose(w2),a1)
    a2 = sigmoid(z2)

    return z1,a1,z2,a2
    
def neural_network(m,n,o,N,X,Y):
    alpha = 0.5
    np.random.seed(1)

    w1 = np.random.randn(n,N)
    w2 = np.random.randn(N,o)

    for i in range(25):
        z1,a1,z2,a2 = FP(w1,w2,X)
        grad1,grad2 = BP(z1,a1,z2,a2,X,Y,w1,w2)
        w1 = w1 - alpha*grad1
        w2 = w2 - alpha*grad2
    
    return w1,w2 

data = pd.read_csv("Logistic_regression_ls.csv")
df = pd.DataFrame(data)

train = df.sample(frac=0.7)
test = df.drop(train.index)

X_train = np.array(train.iloc[:,0:2])
label = np.array(train['label'])

X_test = np.array(test.iloc[:,0:2])
test_label = np.array(test['label'])

m = len(X_train)
n = 2
o = 1

plt.scatter(X_train[:,0],X_train[:,1],c=label)
plt.title('Train Data')
plt.show()
plt.scatter(X_test[:,0],X_test[:,1],c=test_label)
plt.title('Test Data')
plt.show()

N_mat = range(10,100,10)
acc = []

for N in range(10,100,10):
    ans1,ans2 = neural_network(m,n,o,N,X_train,label)
    a,b,c,predict = FP(ans1,ans2,X_test)
    predict = np.transpose(predict)
    p = []
    count = 0
    for j in range(len(predict)):
        if predict[j]>=0.5:
            p.append(1)
        else:
            p.append(0)
        if p[j]==test_label[j]:
            count+=1
    acc.append(count*100/m)
    plt.scatter(X_test[:,0],X_test[:,1],c=p)
    plt.title(str(N)+"units in Hidden layer")
    plt.show()

plt.plot(N_mat,acc,marker='o')
plt.title('Accuracy Plot')
plt.xlabel('Units in hidden layer')
plt.ylabel('Accuracy')
plt.show()
