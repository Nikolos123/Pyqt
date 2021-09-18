from ipaddress import ip_address
from subprocess import Popen, PIPE,call


import socket


def host_ping(list_ip_adress, timeout=10, request=1):
    """
    :param list_ip_adress:
    :param timeout:
    :param request:
    :return:
    """
    result = {'Доступные узлы': '', 'Недоступные узлы': ''}
    for addres in list_ip_adress:
        try:
            address = ip_address(socket.gethostbyname(addres))
            # address = ip_address(address)

        except ValueError:
             # pass
            address = socket.gethostbyname(addres) #Можено
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

        print(res_string)


if __name__ == '__main__':
    ip_adresser = ['ya.ru', 'mail.ru', '2.2.2.2', '192.168.0.2', '192.168.0.1']
    host_ping(ip_adresser)
