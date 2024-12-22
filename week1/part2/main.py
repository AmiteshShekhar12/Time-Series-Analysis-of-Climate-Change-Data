'''
    NumPy and The Matrix
'''
import numpy as np

def task1(matrix):
    '''print the upper diagonal matrix in column-wise fashion'''
    upper_diagonal = np.triu(matrix)
    for col in range(upper_diagonal.shape[1]):
        for row in range(upper_diagonal.shape[0]):
            if row <= col:
                print(upper_diagonal[row, col], end=' ')
    print()
    

def task2(matrix):
    '''print mean, median, std (precision 2), all along x, determinant and inverse/pseudo-inverse'''
    mean_x = np.mean(matrix, axis=0)
    median_x = np.median(matrix, axis=0)
    std_x = np.std(matrix, axis=0)

    print(mean_x)
    print(median_x)
    print(np.round(std_x, 2))

    determinant = np.linalg.det(matrix)
    #print(determinant)

    try:
        inverse = np.linalg.inv(matrix)
        print(np.round(inverse,2))
    except np.linalg.LinAlgError:
        pseudo_inverse = np.linalg.pinv(matrix)
        print(np.round(pseudo_inverse,2))

def task3(matrix):
    '''print after sorting along vertical and horizontal and then print flattened array'''
    sorted_vertical = np.sort(matrix, axis=0)
    sorted_horizontal = np.sort(matrix, axis=1)

    print(sorted_vertical)
    print(sorted_horizontal)

    flattened_array = matrix.flatten()
    flattened_array.sort()
    print(flattened_array)

def task4(matrix):
    '''print the unique frequencies of the sorted array and the frequency of second-largest'''
    flattened_array = matrix.flatten()
    unique_elements, counts = np.unique(flattened_array, return_counts=True)
    sorted_indices = np.argsort(unique_elements)
    sorted_unique_elements = unique_elements[sorted_indices]
    sorted_counts = counts[sorted_indices]

    print(sorted_unique_elements)
    print(sorted_counts)

    if len(sorted_counts) > 1:
        second_largest_freq = sorted_counts[-2]
        print(second_largest_freq)

       
def task5(matrix, num = 0):
    '''print the padded matrix'''
    padded_matrix = np.pad(matrix, pad_width=num, mode='constant', constant_values=0)
    print(padded_matrix)
# You can test these functions on your own and match with the given output in the out folder
