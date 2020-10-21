

def index_all(given_list, searched_value):
    indices = []
    for i, item in enumerate(given_list):
        if type(item) == list:
            for index in index_all(item, searched_value):
                indices.append([i]+index)
        elif searched_value == item:
            indices.append([i])
    return indices


if __name__ == '__main__':
    print(index_all([[[1, 2, 3], 2, [1, 3]], [1, 2, 3]], 3))

