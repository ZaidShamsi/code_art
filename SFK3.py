import pandas as pd
import numpy as np
from sklearn import linear_model

# read the excel dataset as DataFrame
File = pd.read_excel(r'xlsxCsv\ME502_Assignment3_EnrollmentNumber.xlsx', sheet_name = 'पत्रक1')

# define the data/predictors as the pre-set,
# pre-set = independent variables in the dataset
df_Z = File[['bedrooms','bathrooms','sqft_living','sqft_lot','floors','waterfront','view','condition','grade','sqft_above','sqft_basement','yr_built','yr_renovated','sqft_living15']]

# Put the target ('price' of house) in another DataFrame
# target = dependent variable
df_Y = File['price']

# fitting a linear model
lm = linear_model.LinearRegression()
model = lm.fit(df_Z ,df_Y)


# converting data frame object to numpy array
mat_Z = df_Z.to_numpy()
mat_Y = df_Y.to_numpy()

F = np.transpose(Y)
Z = File[['bedrooms','bathrooms','sqft_living','sqft_lot','floors','waterfront','view','condition','grade','sqft_above','sqft_basement','yr_built','yr_renovated','sqft_living15']]
Z = Z.to_numpy()
print(type(Z))
print(np.shape(Z))
B = np.transpose(Z)
print(np.shape(B))
A = np.dot(B,Z)
C = np.linalg.inv(A)
print('Matrix A',A)
print('Matrix C',C)
D = np.dot(B,F)
E = np.dot(C,D)
print('Matrix D',D)
print('Coeff Matrix',E)
