import os
import subprocess
import time

process = []

while True:
    action = input('Выберите действие: q - выход , s - запустить сервер и клиенты, x - закрыть все окна:')

    if action == 'q':
        break
    elif action == 's':

        clients_count = int(input('Введите количество тестовых клиентов для запуска: '))
        #start server
        catalog =  os.getcwd()
        path_server = f'python3 {catalog}/server.py'
        process.append(subprocess.Popen(['konsole','-e',path_server]))

        # Запускаем сервер!
        # process.append(subprocess.Popen(['python' ,'server.py'],stdout = subprocess.PIPE))
        # Запускаем клиентов:
        time.sleep(0.1)
        for i in range(clients_count):
            path_client = f'python3 "{catalog}/client.py" -m listen -u userL{i}'
            process.append(subprocess.Popen(['konsole','-e',path_client]))
            time.sleep(0.1)
            # process.append(
            #     subprocess.Popen(['python','client.py',f'-n test{i + 1}'],stdout = subprocess.PIPE))
    elif action == 'x':
        while process:
            victim = process.pop()
            victim.kill()

