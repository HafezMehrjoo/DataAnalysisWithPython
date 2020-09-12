# Exercise 11 (rows and columns)
def get_rows(array):
    list_of_rows = []
    for i in range(0, array.shape[0]):
        list_of_rows.append(array[i:i + 1, :][0])
    return list_of_rows


def get_columns(array):
    list_of_rows = []
    for i in range(0, array.shape[1]):
        list_of_rows.append(array[:, i])
    return list_of_rows

