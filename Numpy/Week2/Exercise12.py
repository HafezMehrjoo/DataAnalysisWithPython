# Exercise 12 (row and column vectors)
def get_row_vector(array):
    list_of_vector_rows = []
    for i in range(0, array.shape[0]):
        list_of_vector_rows.append(array[i, :].reshape(1, array.shape[0]))
    return list_of_vector_rows


def get_columns_vectors(array):
    list_of_rows = []
    for i in range(0, array.shape[1]):
        list_of_rows.append(array[:, i].reshape(array.shape[1], 1))
    return list_of_rows
