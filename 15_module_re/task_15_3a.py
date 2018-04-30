# -*- coding: utf-8 -*-
"""
Задание 15.3a

Переделать функцию parse_cfg из задания 15.3 таким образом, чтобы она возвращала словарь:
* ключ: имя интерфейса
* значение: кортеж с двумя строками:
  * IP-адрес
  * маска

Например (взяты произвольные адреса):
{'FastEthernet0/1':('10.0.1.1', '255.255.255.0'),
 'FastEthernet0/2':('10.0.2.1', '255.255.255.0')}

Для получения такого результата, используйте регулярные выражения.

Проверить работу функции на примере файла config_r1.txt.

Обратите внимание, что в данном случае, можно не проверять корректность IP-адреса,
диапазоны адресов и так далее, так как обрабатывается вывод команды, а не ввод пользователя.

"""

# import re

# def parse_cfg(config):
#     regex = (r"interface (?P<intf>\S+)"
#              r"| ip address (?P<ip>(\d{1,3}.?){4} ?P<mask>(\d{1,3}.?){4}")
#     with open(config) as f:
#         match = re.finditer(regex, f.read())
#         for m in match:
#             if m.lastgroup == 'intf':
#                 interface = m.group(m.lastgroup)
#     return interface
#
# if __name__ == '__main__':
#     print(parse_cfg('config_r1.txt'))

import re

regex = (r'interface (?P<intf>\S+)'
         r'| ip address (?P<ip>[\d.]+ [\d.]+)')

result = {}

with open('/home/rustok/git/pyneng/15_module_re/config_r1.txt') as f:
    match_iter = re.finditer(regex, f.read())
    for match in match_iter:
        if match.lastgroup == 'intf':
            interface = match.group(match.lastgroup)
            result[interface] = {}
        elif interface:
            result[interface] = tuple(match.group('ip').split())
        a = {key: result[key] for key in result if result[key]}


print(a)