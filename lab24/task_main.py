# Программа считывает данные из файла с успеваемостью студентов
# обрабатывает данные и создает новый файл, который содержит
# результаты по каждому студенту
#
# Version: 1.0
# Group: 10701219
# Author: Колосов Артём Александрович
# Date: 16.4.2020

def output_to_user(msg, s=' ', e='\n'):
    print(msg, sep=s, end=e)


def middle(marks):
    if not isinstance(marks, str):
        return None
    result = 0
    try:
        marks = list(map(int, marks.split()))
        result = sum(marks) / len(marks)
    except ZeroDivisionError as msg:
        output_to_user(msg)
    except ValueError as msg:
        output_to_user(msg)
    except TypeError as msg:
        output_to_user(msg)
    return result


def add_main_data(my_file, data):
    if not isinstance(data, dict):
        return None
    for key in data.keys():
        my_file.write("{0} {1}\n".format(key, get_marks_of_group(data, key)))
        for next_key in data[key]:
            my_file.write("{0} - {1}\n".format(next_key, middle(data[key][next_key])))
        my_file.write("\n")


def get_marks_of_group(data, data_key):
    if not isinstance(data, dict):
        return None
    group_middle = 0
    num = 0
    result = 0
    for next_data_key in data[data_key]:
        group_middle += middle(data[data_key][next_data_key])
        num += 1
    try:
        result = round(group_middle / num, 2)
    except ZeroDivisionError as msg:
        output_to_user(msg)
    return result


def add_best_worse_students(data, my_file, message, mark_key_start=0, mark_key_end=10):
    if not (isinstance(data, dict) and isinstance(message, str)):
        return None
    my_file.write(message + "\n")
    count = 0
    for key in data.keys():
        for next_key in data[key]:
            mark = middle(data[key][next_key])
            if mark_key_start <= mark <= mark_key_end:
                count += 1
                my_file.write("{0}) {1} - {2}\n".format(count, next_key, mark))

    my_file.write("\n")


def get_dict(text):
    if not isinstance(text, list):
        return None
    data = {}
    group_num = ""
    code_word = "группа"
    split_symbol = '-'
    for name in text:
        if code_word in name.lower():
            group_num = name
            data[group_num] = {}
        elif len(name.split(split_symbol)) == 2:
            name = name.split(split_symbol)
            name[0] = name[0].strip()
            name[1] = name[1].strip()
            data[group_num][name[0]] = name[1]
    return data


def main():
    path_in = r"in.txt"
    path_out = r"out.txt"
    encode = "1251"
    try:
        file = open(path_in, "r", encoding=encode)
    except FileNotFoundError as msg:
        output_to_user("Error: {0}".format(msg))
        input()
        exit(1)

    string = file.read().split("\n")

    all_data = get_dict(string)
    new_file = open(path_out, "w", encoding=encode)

    add_main_data(new_file, all_data)

    add_best_worse_students(all_data, new_file, "Студенты, которым надо подсобраться:", 0, 4)
    add_best_worse_students(all_data, new_file, "Лучшие студенты потока:", 9, 10)

    file.close()
    new_file.close()
    input("Programm ended succesfully!")

if __name__ == "__main__":
    main()
