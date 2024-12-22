import numpy as np
my_arr = np.random.randint(1, 101, size=(5, 5))
print(my_arr)
print(f"middle element: {my_arr[2, 2]}")
for i in range(5):
    mean = np.mean(my_arr[i])
    print(f"mean of row {i} is {mean}")

overall_mean = np.mean(my_arr)
new_arr = my_arr[my_arr > overall_mean]
print("New array with elements greater than the overall mean:")
print(new_arr)

def spiral_order (matrix):
    result = []
    left, right = 0, len(matrix[0]) - 1
    top, bottom = 0, len(matrix) - 1

    while left <= right and top <= bottom:
        for col in range(left, right + 1):
            result.append(matrix[top][col])
        top += 1

        for row in range(top, bottom + 1):
            result.append(matrix[row][right])
        right -= 1

        if top <= bottom:
            for col in range(right, left - 1, -1):
                result.append(matrix[bottom][col])
            bottom -= 1

        if left <= right:
            for row in range(bottom, top - 1, -1):
                result.append(matrix[row][left])
            left += 1

    return result

matrix = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]

print(spiral_order(matrix))