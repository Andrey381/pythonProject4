count = 3
password = '123'
userchoice = ''

while True:
    userchoice = input('Введите пароль')
    if password == userchoice:
        print('Доступ разрешён')
        break
    count -= 1
    if count == 0:
        print('Попытки исчерпаны')
        break
    else:
        print('Пароль не верный. Попыток осталось - ' + str(count))

# str(x) - преоброзование X в строку
# int(x) - преоброзование X в целое
# float(x) - преоброзование X в
