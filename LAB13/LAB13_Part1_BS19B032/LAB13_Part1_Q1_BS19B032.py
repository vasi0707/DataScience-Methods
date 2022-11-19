import numpy as np
import matplotlib.pyplot as plt
import random
import math
import pandas as pd

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

    for i in range(10):
        classes = error_class(centroid,x,y)
        centroid = centroid_update(x,y,classes,k)
        x_c = [*(zip(*centroid))]
        y_c = x_c[1]
        x_c = x_c[0]
        plt.scatter(x_c,y_c,color='red',marker='+')
        plt.scatter(x,y,c=classes)
        plt.show()
    
    return centroid,classes

df = pd.read_csv('points.csv')

x = df['x']
y = df['y']
sample = list((zip(x,y)))

ans,classes = kmeans(3,sample,x,y)

print("The final centroids are: ")
print(ans)
