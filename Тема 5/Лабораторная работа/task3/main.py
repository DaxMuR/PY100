from random import sample



def get_unique_list_numbers() -> list[int]:
    randomlist_ = sample(range(-10, 11), 15)
    list_unique_numbers = list(set(randomlist_))
    print(list_unique_numbers)

get_unique_list_numbers()


