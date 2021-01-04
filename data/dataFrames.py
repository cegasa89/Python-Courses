import numpy as np
import pandas as pd

A = [1, 2, 3, 4]
B = [5, 6, 7, 8]
C = [9, 0, 1, 2]
D = [3, 4, 5, 6]
E = [7, 8, 9, 0]

df = pd.DataFrame([A, B, C, D, E], ['a', 'b', 'c', 'd', 'e'], ['W', 'X', 'Y', 'Z'])

# create a new column
print("-----------------------------")
df['P'] = df['Y'] + df['Z']

# remove a row
print("-----------------------------")
df = df.drop('e')

# remove a column
print("-----------------------------")
df1 = df.drop('P' , axis = 1)

print(df1.loc['a'])

print(df1.loc['a','Y'])

#condicional acessing
print("-----------------------------")
print( df > 3)

print( df[df['W'] > 8][['W']])

d = {'a':[1,2,3,4,5],'b':[6,7,8,9,np.nan],'c':[0,1,2,np.nan,np.nan]}
df = pd.DataFrame(d)
print(df)

#drop all row with any na
print("-----------------------------")
print(df.dropna(axis=0))


print(df.fillna(1))


#missing data
print("-----------------------------")
