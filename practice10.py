import numpy as np

list = [1.2, 2, 3.5, 4.7, 5]
array = np.array(list)
print(array)

arr1 = np.arange(1,51).reshape(5,10)
print(arr1)

arr2 = np.ones((5,5))
print(arr2)

arr3 = np.around(np.linspace(2.5, 6.5, 30), 2)
print(arr3)

arr4 = np.full((2,3), 2)
arr5 = np.full((2,3), 3)
arr6 = arr4 * arr5
print(arr6)

arr7 = np.array([[10, 20, 30], [40, 50, 60]])
print(arr7.sum(axis = 0), arr7.sum(axis = 1))

matrix_1 = np.array([[2, -2, -1], [-1, -3, 2], [0, 5, -2]])
matrix_2 = np.array([-6, -5, 10]).reshape(3,1)
print(matrix_2)

solved = np.linalg.solve(matrix_1, matrix_2)
print(np.around(solved).astype(np.int32))

inv = np.linalg.inv(matrix_1)
solved_2 = np.dot(inv, matrix_2)
print(solved_2)