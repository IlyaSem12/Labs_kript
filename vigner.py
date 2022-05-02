def vicode(key, message):
    alph1 = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяабвгдеёжзийклмнопрстуфхцчшщъыьэюя"

    a = message.split()
    messagetxt = ''.join(a).lower() # убираем пробелы
    res = ""
    count = 0
    newkey = key

    if len(messagetxt) > len(key):
        addlet = len(messagetxt) - len(key)
        while addlet != 0:
            if count == len(key):
                count = 0
            newkey = newkey + key[count]
            count += 1
            addlet -= 1

    if len(key) > len(messagetxt):
        for i in range(len(key) - len(messagetxt)):
            messagetxt += ' '


    for i in range(len(messagetxt)):
        indexkey = alph1.find(messagetxt[i])
        indexmess = alph1.find(newkey[i])
        newlet = indexkey + indexmess
        res = res + alph1[newlet]


    # print("str23", res)

    return (res)


def decodevi(key, message):
    alph1 = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяабвгдеёжзийклмнопрстуфхцчшщъыьэюя"

    a = message.split()
    messagetxt = ''.join(a).lower() # убираем пробелы
    res = ""
    res2 = ""
    count = 0
    newkey = key

    if len(messagetxt) > len(key):
        addlet = len(messagetxt) - len(key)
        while addlet != 0:
            if count == len(key):
                count = 0
            newkey = newkey + key[count]
            count += 1
            addlet -= 1


    for i in range(len(messagetxt)):
        indexkey = alph1.find(messagetxt[i])
        indexmess = alph1.find(newkey[i])
        newlet = indexkey - indexmess
        res = res + alph1[newlet]

    # print("str", res)

    return (res)


while True:
    try:
        x = int(input('Выбирите действие\n 1) Зашифровать/расшифровать 2) Выход\n'))

        if x == 1:
            Message = input("Введите сообщение\n")
            Key = input("Введите ключ\n")
            print("Зашифрованное сообщение: ", vicode(Key, Message))
            print("Расшифрованное сообщение: ", decodevi(Key, vicode(Key, Message)))
        elif x == 2:
            break
        else:
            print('нет такого варианта')
    except Exception:
        print("Что-то пошло не так обратитесь в службу поддержки")
