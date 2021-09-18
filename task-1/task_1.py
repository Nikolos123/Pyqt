# 1. Написать функцию host_ping(), в которой с помощью
# утилиты ping будет проверяться доступность сетевых узлов.
# Аргументом функции является список, в котором каждый
# сетевой узел должен быть представлен именем хоста или ip-адресом.
# В функции необходимо перебирать ip-адреса и
# проверять их доступность с выводом соответствующего сообщения
# («Узел доступен», «Узел недоступен»).
# При этом ip-адрес сетевого узла должен создаваться с помощью функции ip_address()

from ipaddress import ip_address
from subprocess import Popen, PIPE


import socket


def host_ping(list_ip_address:list, timeout=10, request=1) -> None or list:
    """
    :param list_ip_address:
    :param timeout:
    :param request:
    :return:
    """
    list_ip = []
    result = {'Доступные узлы': '', 'Недоступные узлы': ''}
    for address in list_ip_address:
        try:
            address = ip_address(socket.gethostbyname(address))
            # address = ip_address(address)

        except ValueError:
             # pass
            address = socket.gethostbyname(address) #Можено
        #заменил флаг n  на c (для линукс)
        args = ["ping", "-c", str(request), "-w", str(timeout), str(address)]
        proc = Popen(args, shell=False, stdout=PIPE)
        proc.wait()

        if proc.returncode == 0:
            result['Доступные узлы'] += f'{str(address)}\n'
            res_string = f'{address}- Узел досутпен'

        else:
            result['Недоступные узлы'] += f'{str(address)}\n'
            res_string = f'{address}- Узел недоступен'
        if __name__ == '__main__':
             print(res_string)
        else:
            list_ip.append(list(res_string.split('-')))

    if __name__ != '__main__':
        return  list_ip


if __name__ == '__main__':
    ip_adresser = ['ya.ru', 'mail.ru', '2.2.2.2', '192.168.0.2', '192.168.0.1']
    host_ping(ip_adresser)
