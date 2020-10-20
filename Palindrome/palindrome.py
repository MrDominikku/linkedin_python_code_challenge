import re


def palindrome_validation(validation_string):
    parse_list = validation_string.split(' ')
    reverse_string = validation_string.replace(' ', '')[::-1]

    if reverse_string == ''.join(map(str, parse_list)):
        return True
    else:
        return False


def only_letters(user_string):
    match = re.search("[^a-zA-Z ]", user_string)
    return match is not None


def main():
    while True:

        user_input = input("Input string for palindrome validation or type 'quit' to exit >>")

        if user_input == 'quit':
            break
        elif only_letters(user_input):
            print('Your string contains other characters than A-Z. Try again.')
        else:
            if palindrome_validation(user_input):
                print('Your string is palindrome.')
            else:
                print('Your string is not palindrome.')


if __name__ == '__main__':
    main()
