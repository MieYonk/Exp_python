import numpy as np
import numpy.linalg

A=np.array([[1,2,3,4],[2,0,6,8],[3,7,1,2],[8,1,1,2]])
print(f"{A=}")
B=np.array([[11,12,13,14],[12,10,16,18],[13,17,11,12],[18,11,10,12]])
print(f"{B=}")
y=np.array([[1],[2],[3],[8]])
print(f"{y=}")
B_1=numpy.linalg.inv(B)
print(f"{B_1=}")
x=A.T*B_1*y
print(f"{x=}")
