import re


def palindrome_validation(validation_string):

    parse_list = re.sub('[^a-zA-Z ]', '', validation_string).split()
    reverse_string = re.sub('[^a-zA-Z]', '', validation_string)[::-1]

    return reverse_string.lower() == ''.join(map(str, parse_list)).lower()


def only_letters(user_string):
    match = re.search("[0-9]", user_string)
    return match is not None


def main():
    while True:

        user_input = input("Input string for palindrome validation or type 'quit' to exit >>")

        if user_input == 'quit':
            break
        elif only_letters(user_input):
            print('Your string contains numbers. Try again.')
        else:
            if palindrome_validation(user_input):
                print('Your string is palindrome.')
            else:
                print('Your string is not palindrome.')


if __name__ == '__main__':
    main()
