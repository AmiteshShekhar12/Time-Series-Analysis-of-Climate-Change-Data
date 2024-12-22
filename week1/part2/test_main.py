import main
import numpy as np
matrix = np.genfromtxt('matrix.csv', delimiter=',', dtype=int)
print(matrix)
print('%'*30)
main.task1(matrix)
print('%'*30)
main.task2(matrix)
print('%'*30)
main.task3(matrix)
print('%'*30)
main.task4(matrix)
print('%'*30)
main.task5(matrix,3)
