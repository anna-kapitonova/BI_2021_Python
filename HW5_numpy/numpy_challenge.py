import numpy as np

# Create 3 arrays using different methods
a = np.array([1, 2, 3, 4, 5])
b = np.zeros(5)
c = np.arange(13)

# Function matrix_multiplication accepts 2 matrixes and multiplies them


def matrix_multiplication(a, b):
    print(a @ b)


# Function multiplication_check accepts a list of matrixes
# and prints "True", if they could be multiplied as they are ordered in the list,
# and "False", if they could not be multiplied


def multiplication_check(list_mat):
    for i in range(len(list_mat)-1):
        if list_mat[i+1].shape[0] != list_mat[i].shape[1]:
            return False
    return True


# Function multiply_matrices accepts a list of matrixes
# and returns a result of multiplication, if it exists,
# or "None", if multiplication is not possible


def multiply_matrices(list_mat):
    new_mat = list_mat[0]
    for i in range(len(list_mat)-1):
        if (list_mat[i+1]).shape[0] != (list_mat[i]).shape[1]:
            return None
        else:
            new_mat = new_mat @ list_mat[i+1]
            print(new_mat)
    return new_mat


# Function compute_2d_distance accepts 2 1d-arrays with coordinates and calculates the distance


def compute_2d_distance(a, b):
    return(np.sqrt((a[0]-b[0])**2+(a[1]-b[1])**2))


# Function compute_multidimensional_distance accepts 2 1d-arrays
# with any number of coordinates (the same in both!) and calculates the distance


def compute_multidimensional_distance(a, b):
    sum_d = 0
    for i in range(len(a)):
        sum_d += (a[i]-b[i])**2
    return np.sqrt(sum_d)


# Function compute_pair_distances accepts 2d arrays,
# where rows are observations and columns are features.
# The function returns the pairwise-distance matrix.


def compute_pair_distances(x):
    return np.sum((x[None, :] - x[:, None])**2, -1)**0.5
