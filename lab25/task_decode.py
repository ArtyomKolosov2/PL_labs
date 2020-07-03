# Программа расшифровывет закодированное сообщение из файла
#
# Version: 1.0
# Group: 10701219
# Author: Колосов Артём Александрович
# Date: 16.4.2020


def decrypt_сaesar(message, shift=1):
    if not isinstance(message, str):
        return None
    alpha_lower = [chr(i) for i in range(ord('a'), ord('z') + 1)]
    alpha_upper = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
    result = ""
    for symbol in message:
        try:
            if symbol in alpha_lower:
                ind = alpha_lower.index(symbol)
                step = ind - shift
                result += alpha_lower[step]
            elif symbol in alpha_upper:
                ind = alpha_upper.index(symbol)
                step = ind - shift
                result += alpha_upper[step]
            else:
                result += symbol
        except IndexError as msg:
            print(msg)
            break
    return result


def find_slice_len(text):
    if not isinstance(text, str):
        return None
    min_index = 0
    minimum = ord(text[0])
    for i in range(len(text)):
        if minimum > ord(text[i]):
            min_index = i
            minimum = ord(text[i])
    return len(text[min_index:])


def decode_additional(decrypt, slice_len):
    if not (isinstance(decrypt, list) and isinstance(slice_len, int)):
        return None
    encrypted_dot_symbol = '/'
    for i in range(len(decrypt)):
        if len(decrypt[i]) > slice_len:
            res = len(decrypt[i]) - slice_len
            decrypt[i] = decrypt[i][res:len(decrypt[i])] + decrypt[i][0:res]
        else:
            res = -slice_len % len(decrypt[i])
            decrypt[i] = decrypt[i][res:] + decrypt[i][0:res]
        if encrypted_dot_symbol in decrypt[i]:
            slice_len += 1


def main():
    path = r"important.txt"
    try:
        file = open(path, "r")
    except FileNotFoundError:
        print("Error: File ", path, " NotFound")
        exit(1)

    text = file.read()
    print(text)
    decrypt = decrypt_сaesar(text, 1).split()
    slice_len = find_slice_len(decrypt[0])
    decode_additional(decrypt, slice_len)
    decrypt = ' '.join(decrypt)

    replace_dict = {'(': '\'',
                    '/': '.\n',
                    '"': '!', 
                    '+': '"'}
    print("="*70)
    for key in replace_dict.keys():
        decrypt = decrypt.replace(key, replace_dict[key])
    print(decrypt)
    input("Press Enter")


if __name__ == "__main__":
    main()
