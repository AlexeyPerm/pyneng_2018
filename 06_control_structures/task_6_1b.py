"""Добавить проверку введенного IP-адреса.
Адрес считается корректно заданным, если он:
состоит из 4 чисел разделенных точкой,
каждое число в диапазоне от 0 до 255.
Если адрес задан неправильно, выводить сообщение:
'Incorrect IPv4 address
"""


ip = input('Введите ip-адрес: ')

incorrect = 'Вы ввели ерунду :) '
correct_ip = False

while not correct_ip:       # Пока НЕ True , повторять цикл
    if len(ip.split('.')) != 4:   # если кол-во октетов в айпишнике не равно 4, то выводится incorrect
        print(incorrect)
        ip = input('Введите ip-адрес ещё раз: ')
    for k in ip.split('.'):       # проходимся по каждому октету и сравниваем его с нужными числами
        if int(k) < 0 or int(k) > 255:
            print(incorrect)
            ip = input('Введите ip-адрес ещё раз: ')
            break
        else:
            correct_ip = True

if correct_ip == True:
    ip_first = int(ip.split('.')[0])    # Берём первый октет
else:
    print("что-то пошло не так")
if ip == '0.0.0.0':
    print('unassigned IP-address')
elif ip_first in range(1, 128):
    print('Class A, unicast')
elif ip_first in range(128, 192):
    print('Class B, unicast')
elif ip_first in range(192, 224):
    print('Class C, unicast')
elif ip_first in range(224, 240):
    print('Class D, multicast')
elif ip == '255.255.255.255':
    print('local broadcast')
else:
    print('unused IP-address')

