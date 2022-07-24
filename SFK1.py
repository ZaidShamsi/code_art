import numpy as np

# Setting the print options to five significant digits
np.set_printoptions(precision=4, suppress= None)

# Defining vec1 and mat 1
vec1 = np.array([-1345.0, 4.5230, -9456.5])
mat1 = np.array([[1.0001, 3.4020, 5.2024],[70000, -9.4020, 0.40202],[4.0000, 6.0202, 83222]])

# Calculationg the product of vec1 and mat1
vec2= vec1*mat1
print("multiplication result of vec1 & mat1 is\n",vec2)

# Calculationg the transpose of mat1
trans_mat1 = np.transpose(mat1)
print('Transpose of mat1 is \n',trans_mat1)

# Calculating the determiant of mat1
determinat_mat1 = np.linalg.det(mat1)
det = np.format_float_scientific(determinat_mat1, precision = 4)

print('Determinant of mat1 is \n', det)

# Trace of mat1
trace_1= np.trace(mat1)
trc = np.format_float_scientific(trace_1, precision = 4)
print('trace of mat1 is \n', trc)
