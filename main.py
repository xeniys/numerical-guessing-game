import random

print('Добро пожаловать в числовую угадайку')


def check_limit(limit):
    if limit.isdigit():
        return True
    else:
        return False


def generate_limit():
    print('Укажите верхнюю границу загаданного числа:')
    right_limit = input()
    while not check_limit(right_limit):
        print("А может быть все-таки введем целое число?")
        right_limit = input()
    return int(right_limit)


def new_game(right_limit):
    print(f'Введите число от 1 до {int(right_limit)}:')
    randomdigit = random.randrange(int(right_limit) + 1)
    usr_d = check_main(right_limit)
    check_digit(usr_d, randomdigit, right_limit)
    return int(randomdigit)


def is_valid(text, right_limit):
    if text.isdigit():
        if int(text) in range(right_limit + 1):
            return True
        else:
            return False
    else:
        return False


def check_main(right_limit):
    user_digit = input()
    while not is_valid(user_digit, right_limit):
        print(f'А может быть все-таки введем целое число от 1 до {right_limit}?')
        user_digit = input()
    return int(user_digit)


def check_digit(usr_d, randomdigit, right_limit):
    count_attempt = 1
    while usr_d != randomdigit:
        count_attempt += 1
        if usr_d < randomdigit:
            print('Ваше число меньше загаданного, попробуйте еще разок')
            usr_d = check_main(right_limit)
        elif usr_d > randomdigit:
            print('Ваше число больше загаданного, попробуйте еще разок')
            usr_d = check_main(right_limit)
    print('Вы угадали, поздравляем!')
    print('Вы угадали число с попытки номер', count_attempt)
    print('Хотите ли вы сыграть еще: д = да, н = нет')
    answer = input()
    while answer.lower() not in ['д', 'н']:
        print("Что-то не так...")
        print('Хотите ли вы сыграть еще: д = да, н = нет')
        answer = input()
    if answer.lower() == 'д':
        right_limit = generate_limit()
        print(f'Загадываю новое число...Введите число от 1 до {right_limit}:')
        new_game(right_limit)
    elif answer.lower() == 'н':
        print('Спасибо, что играли в числовую угадайку. Еще увидимся...')


right_limit = generate_limit()
new_game(right_limit)
