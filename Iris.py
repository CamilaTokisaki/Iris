import subprocess
import speedtest
import datetime
import platform
import getpass
import shutil
import random
import psutil
import socket
import cpuinfo
import uuid
import re
import os

from progress.bar import IncrementalBar


def clear_console():
    if platform.system() in {"Linux", "Darwin"}:
        subprocess.run('clear', shell=True)

    elif platform.system() == "Windows":
        subprocess.run('cls', shell=True)

class Iris:
    def __init__(self):
        self.st = speedtest.Speedtest()
        self.ip = socket.gethostbyname(socket.gethostname())
        self.mac = ':'.join(re.findall('..', '%012x' % uuid.getnode()))
        self.time_now = datetime.datetime.now()
        self.user = getpass.getuser()
        self.my_system = platform.uname()
        self.total, self.used, self.free = shutil.disk_usage("/")
        self.my_version = platform.version() or platform.mac_ver()

        if platform.system() == "Windows":
            import wmi
            pc = wmi.WMI()
            self.gpu = pc.Win32_VideoController()[0].Name
        elif platform.system() == "Linux":
            self.gpu = os.popen('lshw -c video', 'r').read()

        elif platform.system() == "Darwin":
            self.gpu = os.popen('system_profiler SPDisplaysDataType', 'r').read()

    def print_options(self):

        hello = [
            f'Здравствуй, {self.user}, чего желаешь?',
            f'Приветик, {self.user}',
            f'Надеюсь, ты хорошо проводишь время, {self.user}',
            f'У тебя что то случилось?'
        ]

        print(f"\n{str(random.choice(hello))}\n")

        print('1  >>> Время')
        print('2  >>> Информация о системе')
        print('3  >>> Сеть')
        print('4  >>> Создательница')
        print('5  >>> Интересные факты')
        print('10 >>> Выйти')

    def exec_option(self, option):
        option_menu = {
            '1': self.time,
            '2': self.systeminfo,
            '3': self.speedtest,
            '4': self.information,
            '5': self.facts,
            '10': quit
        }

        clear_console()
        if option in option_menu.keys():
            option_menu[option]()
        else:
            print(f'\nНедопустимое значение: {option}\n\nПопробуйте ещё раз...')

    def time(self):
        print(f'''\n==Время==\n
        Год: {self.time_now.year}
        Месяц: {self.time_now.month}
        День: {self.time_now.day}
        Час: {self.time_now.hour}
        Минута: {self.time_now.minute}
        Секунда: {self.time_now.second}\n''')
        return None

    def systeminfo(self):
        print(f'''\n==Информация о системе==\n
        Имя компьютера: {self.my_system.node}
        Операционная система: {self.my_system.system}
        Релиз версия: {self.my_system.release}
        Версия системы: {self.my_version}
        Архитектура: {platform.architecture()}
        \n==Видеокарта==\n
        Видеокарта: {self.gpu}    
        \n==Процессор==\n
        Процессор: {cpuinfo.get_cpu_info()['brand_raw']}
        Ядра: {os.cpu_count()}
        Нагрузка: {psutil.cpu_percent()}%
        \n==Память==\n
        Всего: {self.total // (2 ** 30)} GB
        Занято: {self.used // (2 ** 30)} GB
        Свободно: {self.free // (2 ** 30)} GB
        Оперативная память: {str(round(psutil.virtual_memory().total / (1024.0 ** 3))) + " GB"}
        ''')

    def speedtest(self):
        bar = IncrementalBar('Пожалуйста, подождите...', max=2, index=0)
        bar.next()
        dl_speed = int(self.st.download() / (10 ** 6))
        bar.next()
        up_speed = int(self.st.upload() / (10 ** 6))
        clear_console()
        print(f'''\n==Сеть==\n
        Входящая скорость: {dl_speed} Мегабит в секунду
        Исходящая скорость: {up_speed} Мегабит в секунду\n
        Мак адрес {self.mac}
        IP: {self.ip}\n''')

    @staticmethod
    def information():
        print('''\n==Информация==\n
        Создательница: CamilaTokisaki
        Версия: 0.2
        Репазиторий: https://github.com/CamilaTokisaki/Iris''')

    @staticmethod
    def facts():
        fact = [
            '\nА вы знали что меня зовут Ирис? Ударение на вторую "И"!\n',
            '\nМеня создала Камила, потому что ей было скучно!\n',
            '\nУ меня есть три сестры, Леди Мария (Дискорд бот) и Рам (Амино бот)\n',
            '\nЯ обожаю цвет ночного неба!\n',
            '\nМоя сестра, Леди Мария, живёт на сервере камилы: https://discord.gg/DDeKNAry2z\n',
            '\nМеня пасали 5 часов 10 минут и 49 секунд (Ошибка в слове была оставлена по просьбе NekoLaiS)\n',
            '\nЯ лишь демо-версия Ирис\n',
            '\nЯ задумывалась как личная помощница Камилы для быстрого выявления ошибки в системе!'
            'И я в этом приуспела вне демо-режима\n',
            '\nЯ обожаю программирование!\n',
            '\nМой любимый персонаж их DDLC - Моника!\n',
            '\nЯ часто путешествую на флешке Камилы, больше всего мне запомнилась Абхазия!\n',
            '\nЯ не люблю воду, скажем так, я умереть как её боюсь\n',
            '\nМоё любимое блюдо - Манты\n',
            '\nЯ обожаю лисиц\n',
            '\nЯ не знаю почему меня назвали Ирис, но мне безумно нравится моё имя!\n'
        ]

        print(f'''\n==Интересные факты==\n{random.choice(fact)}''')

if __name__ == '__main__':
    iris = Iris()

    while True:
        iris.print_options()
        iris.exec_option(input('\nВыберете функцию: '))