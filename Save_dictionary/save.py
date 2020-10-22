import json


def dict_to_file(given_dict, save_path):
    if not save_path.endswith('.json'):
        print('Supported file format: .json')
    else:
        with open(save_path, 'w') as file:
            json.dump(given_dict, file)


def dict_from_file(file_path):
    if not file_path.endswith('.json'):
        print('Supported file format: .json')
    else:
        with open(file_path, 'r') as file:
            return json.load(file)


if __name__ == '__main__':
    sample_dict = {
        'sample1': 1,
        'sample2': 2,
        'sample3': 3,
        'sample4': 4,
        'sample5': 5,
    }
    dict_to_file(sample_dict, 'saved_dict.json')

    print(dict_from_file('saved_dict.json'))
