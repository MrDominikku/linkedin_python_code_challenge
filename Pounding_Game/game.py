import random
import time


def waiting_game():
    print("""
            Rules of the game are simple: 
            Initial the game by hitting ENTER.
            Program will randomly select time between 1-5 seconds.
            Hit ENTER again after given time.
            Enjoy!
            """)

    input('Ready when you are!')

    while True:

        wait_time = random.randint(1, 5)
        input('Your target time is %s second. Hit ENTER to start counting!' % wait_time)
        start_time = time.time()
        input('Waiting...')
        end_time = round(time.time() - start_time, 2)
        if abs(wait_time - end_time) == 0.00:
            print('Your time %s seconds. Bullseye! You are truly time master!' % end_time)
        elif abs(wait_time - end_time) < 0.05:
            print('Your time %s seconds. WOW! Almost perfect shot!' % end_time)
        elif abs(wait_time - end_time) < 0.5:
            print('Your time %s seconds. Nice one! Keep practicing!' % end_time)
        else:
            if (wait_time - end_time) > 0.5:
                print('Your time %s seconds. Damn...Too slow! Be more patient!' % end_time)
            elif (wait_time - end_time) < -0.5:
                print('Your time %s seconds. Damn...Too fast! Be more patient!' % end_time)

        if input('Do you want to play again? (Y/N)').lower() != 'y':
            break


if __name__ == '__main__':
    waiting_game()
