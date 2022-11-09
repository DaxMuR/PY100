field = list(range(1, 10))

def print_field(field):
    for i in range(3):
        print("|", field[0 + i * 3], "|", field[1 + i * 3], "|", field[2 + i * 3], "|")

victory_mark = ((0, 1, 2),
                (3, 4, 5),
                (6, 7, 8),
                (0, 3, 6),
                (1, 4, 7),
                (2, 5, 8),
                (0, 4, 8),
                (2, 4, 6)
                )

def check_victory(field):
    for i in victory_mark:
        if field[i[0]] == field[i[1]] == field[i[2]]:
            return field[i[0]]
    return False


def choose_symbol(symbol):
    choose = False
    while not choose:
        symb = input("Ваша очередь ставить: " + symbol + "!")
        symb = int(symb)
        if symb >= 1 and symb <= 9:
            if(str(field[symb-1]) not in "XO"):
                field[symb-1] = symbol
                choose = True
            else:
                print("Поле занято!")
        else:
            print("Такого поля нет! Введите корректный номер!")

def main(field):
    counter = 0
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


