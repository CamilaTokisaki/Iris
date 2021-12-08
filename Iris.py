import subprocess
import speedtest
import datetime
import platform
import getpass
import shutil
import random
import psutil
import socket
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
        self.cpu = psutil.cpu_freq()
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
            self.gpu = os.popen('lshw', 'r').read()

    def print_options(self):
        hello = [
            f'Здравствуй, {self.user}, чего желаешь?',
            f'Приветик, {self.user}',
            f'Надеюсь, ты хорошо проводишь время, {self.user}',
            f'У тебя что то случилось?'
        ]

        print(f"\n{str(random.choice(hello))}\n")

        print('1  >>> Время')
        print('2  >>> Графика')
        print('3  >>> Информация о системе')
        print('4  >>> Память')
        print('5  >>> Сеть')
        print('6  >>> Создательница')
        print('7  >>> Интересные факты')
        print('10 >>> Выйти')

    def exec_option(self, option):
        option_menu = {
            1: self.time,
            2: self.videocard,
            3: self.systeminfo,
            4: self.memory,
            5: self.speedtest,
            6: self.information,
            7: self.facts,
            10: quit
        }

        clear_console()
        if option in option_menu.keys():
            option_menu[option]() 
        else:
            print(f'Недопустимое значение: {option}\nПопробуйте ещё раз...')

    def time(self):
        print("\n==Время==\n")
        print(
            f"\nГод: {self.time_now.year} "
            f"Месяц: {self.time_now.month} "
            f"День: {self.time_now.day} "
            f"Час: {self.time_now.hour} "
            f"Минута: {self.time_now.minute} "
            f"Секунда: {self.time_now.second}\n")
        return None

    def videocard(self):
        print("\n==Видеокарта==\n")
        print(self.gpu, '\n')
        pass

    def systeminfo(self):
        print("\n==Информация о системе==\n")
        print(f"\nИмя компьютера: {self.my_system.node}")
        print(f"Операционная система: {self.my_system.system}")
        print(f"Релиз версия: {self.my_system.release}")
        print(f"Версия системы: {self.my_version}")
        print(f"Архитектура: {self.my_system.machine}")
        print(f"Процессор: {platform.processor()}")
        print(f"Частота процессора: {self.cpu}\n")

    def memory(self):
        print("\n==Память==\n")
        print("Всего: %d GB" % (self.total // (2 ** 30)))
        print("Занято: %d GB" % (self.used // (2 ** 30)))
        print("Свободно: %d GB" % (self.free // (2 ** 30)))
        print("Оперативная память:", str(round(psutil.virtual_memory().total / (1024.0 ** 3))) + " GB\n")

    def speedtest(self):
        bar = IncrementalBar('Измеряю ', max=2, index=0)
        bar.next()
        dl_speed = int(self.st.download() / (10 ** 6))
        bar.next()
        up_speed = int(self.st.upload() / (10 ** 6))
        clear_console()
        print("\n==Сеть==\n")
        print(f"Входящая скорость: {dl_speed} Мегабит в секунду")
        print(f"Исходящая скорость: {up_speed} Мегабит в секунду\n")
        print(f"Мак адрес {self.mac}")
        print(f"IP: {self.ip}\n")

    @staticmethod
    def information():
        print('\n==Информация==\n')
        print('Создательница: CamilaTokisaki')
        print('Версия: 0.1')
        print('Репазиторий: https://github.com/CamilaTokisaki/Iris')

    @staticmethod
    def facts():
        fact = [
            'А вы знали что меня зовут Ирис? Ударение на вторую "И"!',
            'Меня создала Камила, потому что ей было скучно!',
            'У меня есть три сестры, Леди Мария (Дискорд бот) и Рам (Амино бот)',
            'Я обожаю цвет ночного неба!',
            'Моя сестра, Леди Мария, живёт на сервере камилы: https://discord.gg/DDeKNAry2z',
            'Меня пасали 5 часов 10 минут и 49 секунд',
            'Я лишь демо-версия Ирис',
            'Я задумывалась как личная помощница Камилы для быстрого выявления ошибки в системе! '
            'И я в этом приуспела вне демо-режима',
            'Я обожаю программирование!',
            'Мой любимый персонаж их DDLC - Моника!',
            'Я часто путешествую на флешке Камилы, больше всего мне запомнилась Абхазия!',
            'Я не люблю воду, скажем так, я умереть как её боюсь',
            'Моё любимое блюдо - Манты',
            'Я обожаю лисиц',
            'Я не знаю почему меня назвали Ирис, но мне безумно нравится моё имя!'
        ]

        print(f'''\n==Интересные факты==\n{random.choice(fact)}''')

    @staticmethod
    def clear_console():
        if platform.system() in {"Linux", "Darwin"}:
            subprocess.run('clear', shell=True)

        elif platform.system() == "Windows":
            subprocess.run('cls', shell=True)


if __name__ == '__main__':
    iris = Iris()

    while True:
        iris.print_options()
        iris.exec_option(int(input('\nВыберете функцию: ')))
