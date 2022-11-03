#Запрашиваем у пользователя какое количество билетов он хочет преобрести
# Запрашиваем возраст к каждому билету, в цикле формируется сумма заказа
sum_tiket=0
while True:
    try:
        count_tiket = int(input('Введите количество билетов, кторое вы бы хотели преобрести:'))
        if count_tiket<0: raise ValueError()
        print(f'\nКоличество билетов для заказа - {count_tiket}, отлично!\n')

        for i in range(count_tiket):
            age=int(input(f'Введите возраст участника, для билета №{i+1}:'))

            if 25 > age >= 18:
                sum_tiket += 990
            elif age >= 25:
                sum_tiket += 1390
            elif 18 > age > 0:
                sum_tiket
            else:raise ValueError()
    except ValueError:
        print('!!! Введено не корректное значение !!!\n')
        sum_tiket = 0
    else: break
#Вывод суммы заказа и учет скидки, если в заказе больше 3 билетов
if count_tiket > 3:
    discount=sum_tiket/100*10
    print(f'\nСумма вашего заказа, с учетом 10% скидки = {round(sum_tiket-discount)}')
    print(f'Сумма вашей скидки составила = {round(discount)}')
else: print(f'\nСумма вашего заказа = {round(sum_tiket)}')