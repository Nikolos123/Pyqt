from tabulate import tabulate
from task_2 import host_range_ping

def host_range_ping_tab():
    #запрашиваем хосты
    res_dict = host_range_ping()
    print(type(res_dict))
    #выводим в табличном виде
    print(tabulate([res_dict],headers='key',tablefmt='pipe',stralign='center'))

if __name__ =='__main__':
    host_range_ping_tab()