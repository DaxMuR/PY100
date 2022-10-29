first_mark = input("Введите начальную точку: ")
first_mark = first_mark.lower()
second_mark = input("Введите конечную точку: ")
second_mark = second_mark.lower()

flat_job = 1
job_shop = 0.5
shop_park = 0.6
park_flat = 0.3
flat_shop = 0.9
job_park = 0.9
price = 200

def cost(mark):
    a = mark * price
    return(a)


if first_mark == first_mark == "квартира" and second_mark == "работа":
    print("Стоимость поездки составит: ", cost(flat_job), "рублей.")
elif first_mark == "работа" and second_mark == "магазин":
    print("Стоимость поездки составит: ", cost(job_shop), "рублей.")
elif first_mark == "магазин" and second_mark == "парк":
    print("Стоимость поездки составит: ", cost(shop_park), "рублей.")
elif first_mark == "парк" and second_mark == "квартира":
    print("Стоимость поездки составит: ", cost(park_flat), "рублей.")
elif first_mark == "квартира" and second_mark == "магазин":
    print("Стоимость поездки составит: ", cost(flat_shop), "рублей.")
elif first_mark == "работа" and second_mark == "парк":
    print("Стоимость поездки составит: ", cost(job_park), "рублей.")
