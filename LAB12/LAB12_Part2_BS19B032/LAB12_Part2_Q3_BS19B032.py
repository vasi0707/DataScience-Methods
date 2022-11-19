#Creating the Data

import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

e = np.exp(1)
np.random.seed(4)


def pdf(x):
    return 0.5 * (stats.norm(scale=0.25 / e).pdf(x) + stats.norm(scale=4 / e).pdf(x))


y = np.random.normal(scale=0.5, size=(30000))
x = np.random.normal(scale=0.5, size=(30000))
z = np.random.normal(scale=0.1, size=len(x))

density = pdf(x) * pdf(y)
pdf_z = pdf(5 * z)

density *= pdf_z

a = x + y
b = 2 * y
c = a - b + z

norm = np.sqrt(a.var() + b.var())
a /= norm
b /= norm

#PCA

samples = len(a)
X = np.array([*(zip(a,b,c))])         #create sample matrix
mean = X.sum(axis=0)
mean = mean/samples
X_mean = np.zeros(X.shape)

for i in range(samples):
    for j in range(len(X[0])):
        X_mean[i][j] = X[i][j] - mean[j]     #Subtracting mean

P = (np.matmul(np.transpose(X_mean),X))/samples     #Computing P

eigen_value,eigen_vector = np.linalg.eig(P)     #Eigen decomposition

print("The eigen values are:")
print(eigen_value)
print("")
print("The eigen vectors are:")
print(eigen_vector)

U = np.transpose(eigen_vector)

projection = np.dot(X,U)  #Finding Projections

print("The projections are: ")
print(projection)

fig = plt.figure(figsize = (5,5))
ax = plt.axes(projection ="3d")
ax.scatter3D(a,b,c,color="red",marker='+')

x_pca_axis, y_pca_axis, z_pca_axis = 3*eigen_vector
x_pca_plane = np.r_[x_pca_axis[:2], -x_pca_axis[1::-1]]
y_pca_plane = np.r_[y_pca_axis[:2], -y_pca_axis[1::-1]]
z_pca_plane = np.r_[z_pca_axis[:2], -z_pca_axis[1::-1]]
x_pca_plane.shape = (2, 2)
y_pca_plane.shape = (2, 2)
z_pca_plane.shape = (2, 2)
ax.plot_surface(x_pca_plane, y_pca_plane, z_pca_plane)
ax.set_title("PCA")

plt.show()

"""
By comparing the results, we can say that both the method produces same set of eigen vectors.
Also, the plot is identical too.
Finally, the results are same.
"""

