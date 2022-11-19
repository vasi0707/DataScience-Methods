import random
import math
import csv
import matplotlib.pyplot as plt

def points_generator(centre_x,centre_y,radius):
    x = []
    y = []
    
    for i in range(10):
        r = random.uniform(0,radius)
        angle = 2*math.pi*random.random()

        x.append(centre_x + r*math.cos(angle))
        y.append(centre_y + r*math.sin(angle))

    return x,y

x1,y1 = points_generator(3,3,2)
x2,y2 = points_generator(7,7,2)
x3,y3 = points_generator(11,11,2)

x = [*x1,*x2,*x3]
y = [*y1,*y2,*y3]

sample = [*(zip(x,y))]

with open("points.csv",'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['x','y'])
    for i in range(len(sample)):
        csvwriter.writerow(sample[i])

plt.scatter(x1,y1,color='red')
plt.scatter(x2,y2,color='blue')
plt.scatter(x3,y3,color='orange')
plt.title('Random Points')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()
