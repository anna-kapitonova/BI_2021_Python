import numpy as np

# Create 3 arrays using different methods
a = np.array([1, 2, 3, 4, 5])
b = np.zeros(5)
c = np.arange(13)


def matrix_multiplication(a, b):
    ''' accepts 2 matrixes and multiplies them '''

    return(a @ b)


def multiplication_check(list_mat):
    ''' accepts a list of matrixes
    and prints "True", if they could be multiplied as they are ordered in the list,
    and "False", if they could not be multiplied '''

    for i in range(len(list_mat)-1):
        if list_mat[i+1].shape[0] != list_mat[i].shape[1]:
            return False
    return True


def multiply_matrices(list_mat):
    ''' accepts a list of matrixes
    and returns a result of multiplication, if it exists,
    or "None", if multiplication is not possible '''

    if multiplication_check(list_mat) is False:
        return None
    else:
        new_mat = list_mat[0]
        for i in range(len(list_mat)-1):
            new_mat = new_mat @ list_mat[i+1]
        return new_mat


def compute_2d_distance(a, b):
    ''' accepts 2 1d-arrays with coordinates and calculates the distance '''

    return(np.sqrt((a[0]-b[0])**2+(a[1]-b[1])**2))


def compute_multidimensional_distance(a, b):
    ''' accepts 2 1d-arrays with any number of coordinates
    (the same in both!) and calculates the distance '''

    return np.sqrt(sum((a-b)**2))


def compute_pair_distances(x):
    ''' accepts 2d arrays (rows are observations and columns are features),
    returns the pairwise-distance matrix '''

    return np.sum((x[None, :] - x[:, None])**2, -1)**0.5
