
main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
newstr = ''.join(main_str.lower().split())


def get_count_char(str_):
    count = {}
    for let in newstr:
        if let.isalpha():
            if let in count:
                count[let] += 1
            else:
                count[let] = 1
    return count
print(get_count_char(main_str))



    # ...  # TODO посчитать количество каждой буквы в строке в аргументе str_





