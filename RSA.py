import math
def encrypt(mess, p, q):
    alph = " абвгдеёжзийклмнопрстуфхцчшщъыьэюяабвгдеёжзийклмнопрстуфхцчшщъыьэюя"

    n = p * q               #открытый элемент(модуль)
    fn = (p - 1)*(q - 1)    #закрытый элемент
    for i in range(fn):     #открытая экспонента
        if math.gcd(i, fn) == 1 and i > 1:
            e = i
            break
    # (d×e) % fn = 1нужно вычислить число d, обратное е по модулю φ. То есть остаток от деления по модулю φ произведения d×e должен быть равен 1. Запишем это в обозначениях, принятых во многих языках программирования: (d×е)%φ=1.
    for i in range(fn):     #закрытая экспонента
        if (i*e) % fn == 1:
            d = i
            break

    ku = [e, n]
    kr = [d, n]

    res = []
    resultA = []
    resultB = []
    resultC = ""


    for i in range(len(mess)): #преобразование в цифры
        res.append(alph.find(mess[i]))

    for i in range(len(res)): #шифрование
        # res.append(alph.find(mess[i]))
        resultA.append(pow(res[i], ku[0], ku[1]))

    for i in range(len(resultA)): #Почти расшифрование
        # res.append(alph.find(mess[i]))
        resultB.append(pow(resultA[i], kr[0], kr[1]))

    for i in range(len(resultB)): #Расшифрование
        resultC = resultC + alph[resultB[i]]


    print("p=", p, "q=", q, "n=", n, "fn=", fn, "e=", e, "d=", d)
    print("Открытый ключ", ku, "Закрытый ключ", kr)
    print("Исходное", *res)
    print("Зашифрованное", *resultA)
    print("Почти расшифрованное", *resultB)
    print("Расшифрованное", resultC)

    # print("Encrypted Message is: ", c)
    # return c

# message = int(input("Введите сообщение"))
# p = 11
# q = 7
# e = 3


encrypt("тест",17,23)
# print("Тест", gcd_rem_division(352,5))


# print("Original Message is: ", message)
# c = encrypt(message)