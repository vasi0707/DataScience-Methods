import numpy as np
import matplotlib.pyplot as plt
import random
import math
import pandas as pd

def cost_function(centroid,classes,x,y):
    cost = 0
    
    for i in range(len(x)):
        c = classes[i]
        cent = centroid[c]
        cost += math.sqrt((x[i]-cent[0])**2+(y[i]-cent[1])**2)
    cost = cost/len(x)

    return cost

def centroid_update(x,y,clas,k):
    sum_x = [0]*k
    sum_y = [0]*k
    count = [0]*k

    for i in range(len(x)):
        c = clas[i]
        sum_x[c] += x[i]
        sum_y[c] += y[i]
        count[c] += 1

    x_centroid = [sum_x[i]/count[i] for i in range(len(sum_x))]
    y_centroid = [sum_y[i]/count[i] for i in range(len(sum_y))]

    centroid = list(zip(x_centroid,y_centroid))

    return centroid

def error_class(centroid,x,y):
    clas = [] 

    for i in range(len(x)):
        error = []
        for j in range(len(centroid)):
            cent = centroid[j]
            error.append(math.sqrt((x[i]-cent[0])**2+(y[i]-cent[1])**2))
        clas.append(error.index(min(error)))

    return clas

def kmeans(k,samples,x,y):
    centroid = random.sample(samples,k)
    hist = [centroid]

    for i in range(20):
        classes = error_class(centroid,x,y)
        centroid = centroid_update(x,y,classes,k)
        hist.append(centroid)
    
    return centroid,classes

df = pd.read_csv('points.csv')

x = df['x']
y = df['y']
sample = list((zip(x,y)))

cost = []

for i in range(1,6):
    ans,classes = kmeans(i,sample,x,y)
    cost.append(cost_function(ans,classes,x,y))
    x_c = [*(zip(*ans))]
    y_c = x_c[1]
    x_c = x_c[0]
    plt.scatter(x_c,y_c,color='red',marker='+')
    plt.scatter(x,y,c=classes)
    tit = 'K-value is' + str(i)
    plt.title(tit)
    plt.show()

plt.plot([1,2,3,4,5],cost,marker='o',color='red')
plt.title("Cost vs K")
plt.xlabel("K value")
plt.ylabel("Cost")
plt.show()
