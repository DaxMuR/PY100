field = list(range(1, 10))  # Заводим количество ячеек в нашем поле


def print_field(field3):

    """
    :param field3: Принимает ячейки поля
    :return: Игровое поле размером 3 х 3
    """

    for i in range(3):  # Через цикл печатаем поле используя переменную field
        print("|", field3[0 + i * 3], "|", field3[1 + i * 3], "|", field3[2 + i * 3], "|")


victory_mark = ((0, 1, 2),
                (3, 4, 5),
                (6, 7, 8),
                (0, 3, 6),
                (1, 4, 7),  # Заводим список всех возможных выигрышных комбинаций в виде кортежей
                (2, 5, 8),
                (0, 4, 8),
                (2, 4, 6)
                )


def check_victory(field):
    """

    :param field: Принимает игровое поле
    :return: При успешной проверке - символ
    """
    for i in victory_mark:  # через цикл переменной i проходимся по всем комбинациям victory_mark, на наличие совпадений
        if field[i[0]] == field[i[1]] == field[i[2]]:
            return field[i[0]]
    return False


def choose_symbol(symbol):
    """

    :param symbol: Принимает введенный символ пользователя
    :return: Возвращает проверки занятой клетки или числа вне диапазона
    """
    choose = False
    while not choose:
        symb = input("Ваша очередь ставить: " + symbol + "!")  # Запрашиваем у пользователя куда поставить символ
        symb = int(symb)  # Так как нам нужно число, а инпут принимат строку
        if 1 <= symb <= 9:  # Первая проверка на границы введенного числа
            if str(field[symb - 1]) not in "XO":    # Вторая проверка на начилие символа в ячейке
                field[symb - 1] = symbol  # Если ячейка пуская, то передаем значение в аргумент
                choose = True
            else:
                print("Поле занято!")  # Если по 2 проверке поле занято,выведи сообщение
        else:
            print(
                "Такого поля нет! Введите корректный номер!")  # Если по первой проверке введено неверное число,
            # выведи сообщение


def main(field):
    """

    :param field: Принимает игровое поле
    :return: Возвращает результат игры
    """
    counter = 0  # Заводим начальный счетчик ходов
    victory = False
    while not victory:
        print_field(field)
        if counter % 2 == 0:
            choose_symbol("X")
        else:
            choose_symbol("O")
        counter += 1
        result = check_victory(field)
        if result:
            print("Игрок, который играл за " + result + " выиграл!")
            victory = True
            break
        if counter == 9:
            print("Ничья!")
            break
    print_field(field)


main(field)
