import random

not_a_number = "This is not a number. Try again."
correct = 'you guessed correctly!'
too_low = 'Too Low!!!'
too_high = 'too high'


def configure_range(maxRange):
    '''Set the high and low values for the random number'''
    return 1, maxRange


def generate_secret(low, high):
    '''Generate a secret number for the user to guess'''
    return random.randint(low, high)


def get_guess():
    '''get user's guess'''
    try:
        return int(input('Guess the secret number? '))
    except ValueError:
        return 'null'


def check_guess(guess, secret):
    '''compare guess and secret, return string describing result of comparison'''
    if guess == 'null':
        return not_a_number
    if guess == secret:
        return correct
    if guess < secret:
        return too_low
    if guess > secret:
        return too_high


def main():
    while True:
        while True:
            try:
                maxRange = int(input("What range should numbers be generated in? (1 - ?) \n"))
            except ValueError:
                print("Please try again.")
            else:
                break
        (low, high) = configure_range(maxRange)
        secret = generate_secret(low, high)

        guesses = 0
        while True:
            guess = get_guess()
            result = check_guess(guess, secret)
            if (result != correct):
                guesses += 1
            print(result)

            if result == correct:
                print("Guesses: " + str(guesses))
                break
        playAgain = input("Would you like to play again? (Y/N)\n")
        if playAgain in ["Yes", "yes", "Y", "y"]:
            print("==========")
            continue
        else:
            break

if __name__ == '__main__':
    main()
