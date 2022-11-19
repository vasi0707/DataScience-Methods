#creating matrices

mat1 = [[1,2,3],[4,5,6],[7,8,9]]
mat2 = [[11,12,13],[14,15,16],[17,18,19]]

#transpose without zip

mat1_trans = [[mat1[0][i],mat1[1][i],mat1[2][i]] for i in range(3)]
print("Transposing mat1 without zip")
print(mat1_trans)
print("")

#transpose with zip
mat2_trans = zip(*mat2)
print("Transposing mat2 with zip")
print(*mat2_trans)
print("")

#addition without zip

mat_add = [[mat1[i][j]+mat2[i][j] for i in range(3)] for j in range(3)]
print("addition without zip")
print(mat_add)
print("")

#addition with zip

mat_add_zip = [val1+val2 for rowa,rowb in zip(mat1,mat2) for val1,val2 in zip(rowa,rowb)]
print("addition using zip")
print(mat_add_zip)
print("")

#subraction without zip

mat_sub = [[mat2[i][j]-mat1[i][j] for i in range(3)] for j in range(3)]
print("subtraction without zip")
print(mat_sub)
print("")

#subtraction with zip

mat_sub_zip = [val1-val2 for rowa,rowb in zip(mat1,mat2) for val2,val1 in zip(rowa,rowb)]
print("subtraction using zip")
print(mat_sub_zip)
print("")

#trace without zip

trace1 = [mat1[i][i] for i in range(3)]
print("Trace of mat1")
print(sum(trace1))
print("")

#trace with zip

tot_mat = [y for x in zip(*mat2) for y in x]
trace2 = [tot_mat[i] for i in range(0,len(tot_mat),4)]
print("Trace of mat2")
print(sum(trace2))
