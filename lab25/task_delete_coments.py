# Программа удаляет комментарии из кода Python
#
# Version: 1.0
# Group: 10701219
# Author: Колосов Артём Александрович
# Date: 16.4.2020

def delete_comments_safe_way(code_lines):
    if not isinstance(code_lines, list):
        return None
    for i in range(len(code_lines)):
        if isinstance(code_lines[i], str):
            flag = False
            prom = list(code_lines[i])
            for j in range(len(prom)):
                if prom[j] == '#':
                    flag = True
                if flag and prom[j] != '\n':
                    prom[j] = ''
            code_lines[i] = "".join(prom)


def delete_comments_faster_way(code_lines):
    if not isinstance(code_lines, list):
        return None

    for i in range(len(code_lines)):
        if isinstance(code_lines[i], str):
            flag = False
            prom = list(code_lines[i])
            start_index = 0
            for j in range(len(code_lines[i])):
                if prom[j] == '#':
                    flag = True
                    start_index = j
                    break
            if flag:
                code_lines[i] = code_lines[i][0:start_index] + '\n'


def main():
    path_in = r"code.in.txt"
    path_out = r"code.out.txt"
    try:
        file = open(path_in, "r")
    except FileNotFoundError:
        print("Error: FileNotFound!")
        exit(1)

    print("1 - Safe Mode\n"
          "2 - Fast Mode")
    command = input("Choose Delete Mode: ")
    all_lines = file.readlines()
    file.close()
    print(''.join(all_lines))
    print("="*50)
    if command == "1":
        delete_comments_safe_way(all_lines)
        print(''.join(all_lines))
        
    elif command == "2":
        delete_comments_faster_way(all_lines)
        print(''.join(all_lines))
    new_file = open(path_out, "w")

    new_file.writelines(all_lines)
    new_file.close()
    input("Press Enter")


if __name__ == "__main__":
    main()
