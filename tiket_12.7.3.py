per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
#print('Банк ТКБ - процентная ставка',per_cent['ТКБ'],'годовых')
list1=list(per_cent.values())
deposit=[]

money = float(input('Введите сумму для вклада:'))
print('money =',int(money))

for i in list1:
    deposit.append(round(money * i/100))

print('deposit =',deposit)
print('Максимальная сумма, которую вы можете заработать —',max(deposit))