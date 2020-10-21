import re


def sort_string(user_str, reverse_order=False):
    parse_list = re.sub('[^a-zA-Z0-9 ]', '', user_str).split()
    parse_dict = {item.lower(): item for item in parse_list}
    sorted_list = sorted(parse_dict, reverse=reverse_order)
    return [parse_dict[key] for key in sorted_list]


def main():
    while True:

        user_input = input("Input string for sorting or type 'quit' to exit >>")

        if user_input == 'quit':
            break
        else:
            print(sort_string(user_input))


if __name__ == '__main__':
    main()
