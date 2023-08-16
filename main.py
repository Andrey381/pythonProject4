# Срез подчиняется системе sss

a = ['Первый', 'Второй']
members = 10

for x in (range(members)):
    print(a[x % 2])

print('Расчет окончен')
