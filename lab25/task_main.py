# Программа Подсчитывает кол-во повторений
# Каждого слова в тексте, и выводит результаты
# в новый файл
#
# Version: 1.0
# Group: 10701219
# Author: Колосов Артём Александрович
# Date: 16.4.2020

def output_to_user(msg, s=' ', e='\n'):
    print(msg, sep=s, end=e)


def isalpha_mod(string):
    result = False
    if isinstance(string, str):
        result = str.isalpha(string) or string == "’" or string == "'"
    return result

def get_words(text):
    if not isinstance(text, str):
        return None
    all_words = {}
    time_text = []
    flag = False
    for symbol in text:
        if isalpha_mod(symbol):
            time_text.append(symbol)
            flag = True
        elif flag:
            string = "".join(time_text)
            if all_words.get(string):
                all_words[string] += 1
            else:
                all_words[string] = 1
            time_text.clear()
            flag = False
    return all_words


def main():
    try:
        path = r"lab25_1_in.txt"
        file = open(path, "r")
    except FileNotFoundError:
        output_to_user("Error: FileNotFound!")
        exit(1)

    text = file.read()
    text_words = get_words(text)
    
    new_file = open("out.txt", "w")

    if isinstance(text_words, dict):
        repet = list(zip(text_words.values(),text_words.keys()))
        repet.sort()
        for i in range(0, len(repet)):
            new_file.write("{0} - {1}\n".format(repet[i][1], repet[i][0]))
        new_file.close()
    input("Task Ended Sucessfully!Press Enter")


if __name__ == "__main__":
    main()
