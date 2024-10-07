#!/usr/bin/env python3
import sys
from art import *

def connect_to_router(hostname, username, password):
    """Функция для подключения к роутеру через SSH"""
    import paramiko  # Импортируем, когда действительно нужно
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        client.connect(hostname, username=username, password=password)
        return client
    except Exception as e:
        print(f"Не удалось подключиться к роутеру: {e}")
        return None

def reboot_router(client):
    """Функция для перезагрузки роутера"""
    stdin, stdout, stderr = client.exec_command("reboot")
    error = stderr.read().decode()
    if error:
        print(f"Ошибка при перезагрузке: {error}")
    else:
        print("Роутер перезагружается...")

def power_off_router(client):
    """Функция для выключения роутера"""
    stdin, stdout, stderr = client.exec_command("poweroff")
    error = stderr.read().decode()
    if error:
        print(f"Ошибка при выключении роутера: {error}")
    else:
        print("Роутер выключается...")

def get_status(client):
    """Функция для получения статуса роутера"""
    stdin, stdout, stderr = client.exec_command("uptime")
    output = stdout.read().decode()
    error = stderr.read().decode()
    if error:
        print(f"Ошибка при получении статуса: {error}")
    else:
        # Изменяем вывод статуса роутера
        status_parts = output.strip().split(",")
        uptime = status_parts[0].strip()  # Время
        active_time = status_parts[1].strip()  # Активное время
        print(f"Статус роутера: {uptime} - Активен уже {active_time}")

def vpn_control(client):
    """Функция для управления VPN-интерфейсом awg0"""
    while True:
        print("\nУправление VPN интерфейсом awg0:")
        print("1. Включить VPN ")
        print("2. Выключить VPN ")
        print("3. Статус VPN ")
        print("4. Назад")

        choice = input("Введите номер команды: ")

        if choice == "1":
            stdin, stdout, stderr = client.exec_command("ifup awg0")
            error = stderr.read().decode()
            if error:
                print(f"Ошибка при включении VPN: {error}")
            else:
                print("VPN включен !")
        elif choice == "2":
            stdin, stdout, stderr = client.exec_command("ifdown awg0")
            error = stderr.read().decode()
            if error:
                print(f"Ошибка при выключении VPN: {error}")
            else:
                print("VPN выключен !")
        elif choice == "3":
            stdin, stdout, stderr = client.exec_command("ip link show awg0")
            output = stdout.read().decode()
            if "UP" in output:
                print("VPN интерфейс активен !")
            else:
                print("VPN интерфейс не активен !")
        elif choice == "4":
            print("Возврат в главное меню...")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

def main():
    # Отобразить ASCII арт
    rcs = text2art("RCS", font='block', chr_ignore=True)
    print(rcs)
    username = 'root'

    # Добавляем 4 попытки подключения
    max_attempts = 4
    attempt = 0
    client = None

    while attempt < max_attempts:
        hostname = input("Введите IP адрес роутера: ")
        password = input("Введите пароль: ")

        client = connect_to_router(hostname, username, password)
        if client:
            welcome_rcs = text2art("WELCOME !", font='block', chr_ignore=True)
            print(welcome_rcs)
            break  # Успешное подключение, прерываем цикл
        else:
            attempt += 1
            print(f"Попытка {attempt} из {max_attempts} не удалась. Попробуйте снова.\n")

    if not client:
        print("Превышено максимальное количество попыток подключения. Программа завершена.")
        sys.exit(1)

    # Основное меню программы
    while True:
        print("\nВыберите команду:")
        print("1. Reboot (Перезагрузить роутер)")
        print("2. OFF (Выключить роутер)")
        print("3. STATUS (Статус роутера)")
        print("4. VPN (Управление VPN-интерфейсом)")
        print("5. EXIT (Выйти из программы)")

        choice = input("Введите номер команды: ")

        if choice == "1":
            reboot_router(client)
        elif choice == "2":
            power_off_router(client)
        elif choice == "3":
            get_status(client)
        elif choice == "4":
            vpn_control(client)
        elif choice == "5":
            print("Выход из программы...")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

    client.close()

if __name__ == "__main__":
    main()

