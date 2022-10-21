uslog = input('Введите логин: ')
uspass = input("Введите пароль: ")
users = {'qq1q': '1q2w345',
         'w2ww': '54e32r1',
         'ee3e': '67y8t90',
         'r4rr': '13q57v9'
}
for i, j in users.items():
    if uslog == i and uspass == j:
        print("Доступ разрешен")
        break
    if uslog != i or uspass != j:
        print("Неверные данные, попробуйте ещё раз!")
        break