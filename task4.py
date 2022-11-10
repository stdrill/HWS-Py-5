# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

with open ('file1.txt', 'r') as file:
    text = file.read()
    print(text)

def encoding(text):
    new_text = ''
    i = 0
    while i < len(text):
        count = 1
        while i + 1 < len(text) and text[i] == text[i + 1]:
            count += 1
            i += 1
        new_text += str(count) + text[i]
        i += 1
    return new_text

new_text = encoding(text)
print(new_text)

with open('file2.txt', 'w') as file:
    file.write(f'{new_text}')

def decoding(new_text):
    decode_text = ''
    count = ''
    for char in new_text:
        if char.isdigit():
            count += char
        else:
            decode_text += char * int(count)
            count = ''
    return decode_text

decode = decoding(new_text)
with open('file1.txt', 'w') as file:
    file.write(f'{decode}')