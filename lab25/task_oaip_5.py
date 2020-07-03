# Программа подсчитывает кол-во символов в диапазоне от 'g' до 'o'
# Подсчитывает кол-во каждого символа в тексте
# Находит предложения, разделённые с двух сторон запятыми и
# Сортирует их по алфавиту
# Считает кол-во слов, разделённых с двух сторон пробелами
# Version: 1.0
# Group: 10701219
# Author: Колосов Артём Александрович
# Date: 16.4.2020

def output_to_user(msg, s=' ', e='\n'):
    print(msg, sep=s, end=e)


def count_symbol_codes(string, symb_one='g', symb_two='o'):
    if not (isinstance(string, str) and  isinstance(symb_one, str) or  isinstance(symb_two, str)):
        return None
    count = 0
    first_code = ord(symb_one)
    second_code = ord(symb_two)
    for symbol in string:
        if first_code <= ord(symbol) <= second_code:
            count += 1
    return count


def count_symbol_alternate(string, symbol_one='g', symbol_two='o', key=lambda s: s):
    if not (isinstance(string, str) and isinstance(symbol_one, str) and isinstance(symbol_two, str)):
        return None
    first_code = ord(key(symbol_one))
    second_code = ord(key(symbol_two))
    for code in range(first_code, second_code + 1):
        output_to_user("Symbol {0} : {1}".format(chr(code), string.count(key(chr(code)))))


def selection_sort(text):
    if not isinstance(text, list):
        return None
    index = 0
    for i in range(len(text) - 1):
        index = i
        for j in range(i + 1, len(text)):
            if strcmp(text[j], text[index]) < 0:
                index = j
        if index != i:
            text[i], text[index] = text[index], text[i]

    return text


def strcmp(str1, str2):
    if not (isinstance(str1, str) and isinstance(str2, str)):
        return None
    smallest_len = len(str1) if len(str1) <= len(str2) else len(str2)
    return_code = 0
    str1 = str1.strip()
    str2 = str2.strip()
    for i in range(0, smallest_len):
        if str1[i] != str2[i]:
            return_code = 1 if ord(str1[i]) > ord(str2[i]) else -1
            break
    return return_code


def count_spaces(my_text):
    if not isinstance(my_text, str):
        return None
    count = 0
    for i in range(len(my_text)):
        if my_text[i].isspace():
            flag = False
            for j in range(i + 1, len(my_text)):
                if my_text[j].isalpha():
                    flag = True
                elif my_text[j].isspace():
                    if flag:
                        count += 1
                        i += j
                    break
                elif my_text[j] in (",", ".", "?", ":", ";", "/"):
                    i += j
                    break
    return count


def main():
    split_symbol = '+'
    try:
        file = open("oaip_file.txt", "r")
        info = file.read().split(split_symbol)
        phrase = info[0]
        text = info[1]
        flag = True
    except FileNotFoundError as msg:
        output_to_user("Error:{0}".format(msg))
        input()
        exit(1)
    except IndexError as msg:
        output_to_user("Error:{0}".format(msg))
        input()
        exit(1)
    
    output_to_user("First Task:")
    output_to_user("Your String: {0}".format(phrase))
    count_symbol_alternate(phrase)
    
    output_to_user("="*50)
    
    output_to_user("Second Task:")
    count_symbol_alternate(text, key=lambda s: s.lower(), symbol_one='a', symbol_two='z')
    text = text.replace("\n", "")
    words = text.split(",")
    words = words[1:len(words) - 1]
    output_to_user("="*50)
    output_to_user("Amount of words, separeted by spaces: {0}".format(count_spaces(text)))
    output_to_user("="*50)
    output_to_user("Sorted Words, separated by commas")
    words = selection_sort(words)
    for word in words:
        output_to_user(word)
    input("Press Enter")

if __name__ == "__main__":
    main()
