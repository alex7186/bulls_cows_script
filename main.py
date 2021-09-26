from random import randint

def generate_number():
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    number1 = numbers[randint(1, len(numbers)-1)]
    numbers.remove(number1)

    number2 = numbers[randint(0, len(numbers)-1)]
    numbers.remove(number2)

    number3 = numbers[randint(0, len(numbers)-1)]
    numbers.remove(number3)

    number4 = numbers[randint(0, len(numbers)-1)]
    numbers.remove(number4)

    return number1 + number2 + number3 + number4


def check_count(number:str):
    return len(list(number)) == len(set(number)) and len(number) == 4


def get_bulls_cows(number:str, real_number:str):
    bulls = 0
    cows = 0

    for i, el in enumerate(number):
        if (el in real_number) and el == real_number[i]:
            bulls += 1

        elif (el in real_number) and el != real_number[i]:
            cows += 1

    return bulls, cows


def make_try(input_number:str, real_number:str):

    bulls, cows = get_bulls_cows(input_number, real_number)
    print('bulls\t{}\ncows\t{}'.format(bulls, cows))

    return bulls, cows


number_of_attempts = 0
guessed = False
game_started = False
real_number = generate_number()


while number_of_attempts < 40 and not guessed:

    number_of_attempts += 1
    if not game_started:
        print('\nthis is the bulls and cows game.\n\nlogic game in which the player must determine the hidden number in the least number of attempts\nhttps://en.wikipedia.org/wiki/Bulls_and_Cows\n')
        game_started = True

    print('attempt #{}'.format(number_of_attempts))
    input_number = str(input('enter a four-digit number without repeating digits\n--> '))

    if not check_count(input_number):
        print('uncorrect number. try again\n')
        number_of_attempts -= 1
        continue

    bulls, cows = make_try(input_number, real_number)

    guessed = bulls == 4
    print()
    if guessed:
        print('congratulations. you guessed the number {} in {} attempts'.format(
            real_number, number_of_attempts))
