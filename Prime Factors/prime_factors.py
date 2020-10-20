

def get_prime_factor(number_given, prime_numbers):
    prime_factors = []
    factors_not_found = True
    while factors_not_found:
        if number_given == 1:
            factors_not_found = False
        else:
            for prime_number in prime_numbers:
                mod_number = number_given % prime_number
                if mod_number == 0:
                    prime_factors += [prime_number]
                    number_given = int(number_given / prime_number)
                    break
    return print('Prime factors for given number are: ' + ', '.join(map(str, [i for i in prime_factors])))


def prime_numbers_generator(upper_limit):
    prime_numbers = []
    for num in range(2, upper_limit + 1):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                prime_numbers += [num]
    return prime_numbers


def main():
    while True:
        user_input = input("Pick any number to get prime factors or type 'quit' to exit >>")
        try:
            if user_input == 'quit':
                break
            elif int(user_input) == 1:
                print('Number given must be higher than 1')
            else:
                get_prime_factor(int(user_input), prime_numbers_generator(int(user_input)))
        except ValueError:
            print('Input provided is not an integer. Try again.')


if __name__ == '__main__':
    main()
