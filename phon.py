def work_with_phonebook():
    choice = show_menu()
    phone_book = read_txt('phoneBook.txt')

    while (choice != 8):
        if choice == 1:
            print_result(phone_book)
        elif choice == 2:
            last_name = input('Введите Фамилию искомого пользователя: ')
            print(find_by_lastname(phone_book, last_name))
        elif choice == 3:
            last_name = input(
                'Введите Фамилию пользователя для смены номера телефона: ')
            new_number = input('Введите новый номер телефона: ')
            print(change_number(phone_book, last_name, new_number))
        elif choice == 4:
            lastname = input(
                'Введите Фамилию пользователя, чью запись требуется удалить: ')
            print(delete_by_lastname(phone_book, lastname))
        elif choice == 5:
            number = input(
                'Введите номер телефона для поиска данных о пользователе: ')
            print(find_by_number(phone_book, number))
        elif choice == 6:
            user_data = input(
                'Введите данные о пользователе через запятую (Фамилия, Имя, Телефон, Описание): ')
            add_user(phone_book, user_data)
            write_txt('phoneBook.txt', phone_book)
        elif choice == 7:
            copy_line_from_file()
        choice = show_menu()


def show_menu():
    while True:
        try:
            choice = int(input("Выберите действие 1-8: \n 1 - Показать телефонную книгу \n 2 - Поиск по Фамилии \n 3 - Изменить номер \n 4 - Удалить по Фамилии \n 5 - Поиск по номеру \n 6 - Добавить пользователя \n 7 - Копировать запись в другой файл \n 8 - Выход \n : "))
            if 1 <= choice <= 8:
                return choice
            else:
                print("Некорректный ввод. Введите число от 1 до 8.")
        except ValueError:
            print("Некорректный ввод. Введите число от 1 до 8.")


def read_txt(filename):
    phone_book = []
    fields = ['Фамилия', 'Имя', 'Телефон', 'Описание']
    with open(filename, 'r', encoding='utf-8') as phb:
        for line in phb:
            record = dict(zip(fields, [value.strip()
                          for value in line.split(',')]))
            phone_book.append(record)
    return phone_book


def write_txt(filename, phone_book):
    with open(filename, 'w', encoding='utf-8') as phout:
        for record in phone_book:
            line = ','.join(record.values())
            phout.write(f'{line}\n')


def copy_line_from_file():
    source_file = input("Введите имя файла, откуда копировать: ")
    destination_file = input("Введите имя файла, куда копировать: ")
    phone_book = read_txt('phoneBook.txt')
    print_result(enumerate(phone_book, 1))
    line_number = int(input("Введите номер строки для копирования: "))

    try:
        with open(source_file, 'r', encoding='utf-8') as source:
            lines = source.readlines()
            if 1 <= line_number <= len(lines):
                with open(destination_file, 'a', encoding='utf-8') as destination:
                    destination.write(lines[line_number - 1])
                print("Запись успешно добавлена в новый файл.")
                write_txt(destination_file, phone_book)
            else:
                print("Некорректный номер строки.")
    except FileNotFoundError:
        print("Указанный файл не найден.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


def print_result(phone_book):
    for record in phone_book:
        print(record)


def find_by_lastname(phone_book, last_name):
    result = [record for record in phone_book if record['Фамилия'] == last_name]
    return result if result else 'Запись не найдена'


def change_number(phone_book, last_name, new_number):
    for record in phone_book:
        if record['Фамилия'] == last_name:
            record['Телефон'] = new_number
            write_txt('phoneBook.txt', phone_book)
            return 'Номер успешно изменен'
    return 'Запись не найдена'


def delete_by_lastname(phone_book, last_name):
    for record in phone_book:
        if record['Фамилия'] == last_name:
            phone_book.remove(record)
            write_txt('phoneBook.txt', phone_book)
            return 'Запись успешно удалена'
    return 'Запись не найдена'


def find_by_number(phone_book, number):
    result = [
        record for record in phone_book if 'Телефон' in record and record['Телефон'] == number]
    return result if result else 'Запись не найдена'


def add_user(phone_book, user_data):
    fields = ['Фамилия', 'Имя', 'Телефон', 'Описание']
    new_record = dict(zip(fields, [value.strip()
                      for value in user_data.split(',')]))
    phone_book.append(new_record)
    write_txt('phoneBook.txt', phone_book)
    print('Пользователь успешно добавлен')


work_with_phonebook()
