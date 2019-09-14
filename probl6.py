sk=ks=0
for i in range(101):
    sk+=i**2
    ks+=i
print('Сумма квадратов=',sk)
ks**=2
print('Квадрат суммы=',ks)
print('Разница=',ks-sk)