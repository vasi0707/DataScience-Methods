import numpy as np

mat1 = [[1,2,3],[4,5,6],[7,8,9]]
mat2 = [[11,22,33],[1,3,5],[34,4,0]]

mat1 = np.array(mat1)
mat2 = np.array(mat2)

vec1 = [2,4,5]
vec2 = [1,3,8]

vec1 = np.array(vec1)
vec2 = np.array(vec2)

print("Matrix 1")
print("")
print(mat1)
print("")
print("Matrix 2")
print("")
print(mat2)
print("")

print("Addition of matrix")
mat3 = mat1+mat2
print("")
print(mat3)
print("")

print("Subtraction of matrix")
mat4 = mat2-mat1
print("")
print(mat4)
print("")

print("Element wise multiplication of matrix")
mat5 = mat1*mat2
print("")
print(mat5)
print("")

print("Multiplication of matrix")
mat6 = mat1@mat2
print("")
print(mat6)
print("")

print("Dot product of matrix")
mat7 = np.dot(mat1,mat2)
print("")
print(mat7)
print("")

print("Vector 1")
print("")
print(vec1)
print("")
print("Vector 2")
print("")
print(vec2)
print("")

print("Addition of vectors")
vec3 = vec1+vec2
print("")
print(vec3)
print("")

print("Subtraction of vectors")
vec4 = vec2-vec1
print("")
print(vec4)
print("")

print("Dot product of vectors")
vec5 = np.dot(vec1,vec2)
print("")
print(vec5)
print("")

print("Cross product of vectors")
vec6 = np.cross(vec1,vec2)
print("")
print(mat6)
print("")

print("Scalar multiplication of vector")
vec7 = 2*vec1
vec8 = 2*vec2
print("")
print(vec7)
print(vec8)
print("")
