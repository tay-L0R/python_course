weight = [100, 800, 75, 90]
height = [1.85, 1.9, 1.75, 2.00]
BMI = []

for i,j in zip(weight, height):
    BMI.append(round(i/(j**2), 2))
print(BMI)
    
    
import numpy as np
weight2 = np.array(weight)
height2 = np.array(height)
BMI = np.around(weight2 / height2**2, 2)
print(BMI)


arr2 = np.array([[1,2,3], [3,8,2], [2,2,5]])
print(np.linalg.det(arr2))


arr4 = np.array([1,2,3,4,5])
print(arr4[-2:])

arr3 = np.around(np.linalg.inv(arr2), 2)
print(arr3)

arr5 = np.zeros((5,5))
for i, j in zip(range(5), range(5)):
    arr5[i,j] = 100
print(arr5)

x = np.linspace(0,10,20).reshape(5,4)
print(x.shape)