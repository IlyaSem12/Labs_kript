from tkinter import *
from tkinter import messagebox as mb
from tabulate import tabulate
window = Tk()
window.title("Шифр перестановки")
window.resizable(False,False)


def cripto(key, message):
    encodemas = []
    tabl = []
    cipher = {}
    result = ' '
    count = 0
    a = message.split()
    messagetxt = ''.join(a).lower()

    if len(key) > len(messagetxt):
        for i in range(len(key) * 2 - len(messagetxt)):
            messagetxt += '_'

    if len(messagetxt) % len(key) != 0:
        while len(messagetxt) % len(key) != 0:
            messagetxt += '_'

    stroki = len(messagetxt) // len(key)

    for index, ch in enumerate(key.lower()):
        if ch in cipher:
            cipher[ch] += messagetxt[index * stroki: index * stroki + stroki]
        else:
            cipher[ch] = messagetxt[index * stroki: index * stroki + stroki]


    print(cipher)
    print(tabulate(cipher.items(), tablefmt="grid"))
    text2.insert(1.0, tabulate(cipher.items(), tablefmt="grid") + '\n')


    for index in range(stroki):
        for i in sorted(key.lower()):
            encodemas.append([cipher[i][index]])
            count += 1
            if count == stroki:
                encodemas.append(" ")
                count = 0

    for i in range(len(encodemas)):
        result += str(*encodemas[i])
    result = result.split()

    for i in range(stroki):
        tabl.append([])
        tabl[i] += messagetxt[i * len(key): i * len(key) + len(key)]


    for i in range(len(result)):
        # messagetxt += message[i]
        txt = ''.join(result).lower()

    text.insert(1.0, txt  + '\n')

    return result


#######################################################

def decripto(key, message):
    encodemas = []
    decodemas = []
    cipher = {}
    result = ' '
    count = 0
    a = message.split()
    messagetxt = ''.join(a).lower()  # убираем пробелы


    sortkey = sorted(key.lower())
    stroki = len(messagetxt) // len(key)

    for i in range(stroki):
        decodemas.append([])
        decodemas[i] += messagetxt[i * len(key): i * len(key) + len(key)]

    destr = ""

    for i in range(len(key)):
        for j in range(stroki):
            destr += decodemas[j][i]

    print("destr", destr)

    for index, ch in enumerate(sortkey):
        if ch in cipher:
            cipher[ch] += destr[index * stroki: index * stroki + stroki]
        else:
            cipher[ch] = destr[index * stroki: index * stroki + stroki]

    for i in key.lower():
        encodemas.append([cipher[i]])
        count += 1

    for i in range(len(encodemas)):
        result += str(*encodemas[i])
    result = result.split()

    for i in range(len(result)):
        # messagetxt += message[i]
        txt = ''.join(result).lower()

    text.insert(1.0, txt + '\n')

    return result

##############кнопки#########################################################

lbl= Label(window,text="Введите текст:").grid(column=0,row=0,pady=8, padx=8,sticky=W)
lbl2= Label(window,text="Введите ключ:").grid(column=0,row=1,pady=8, padx=8,sticky=W)


entr_txt=Entry(window,width=30)
entr_txt.grid(column=1,row=0,columnspan=3,pady=8, padx=8,sticky=W)
entrkey=Entry(window,width=15)
entrkey.grid(column=1,row=1,pady=8, padx=8,sticky=W)

btn_go = Button(window, text="жмак")
btn_go.grid(column=2, row=1, pady=8, padx=8, sticky=W)


r_var = IntVar()
r_var.set(0)
r1 = Radiobutton(text='Зашифровать',
                 variable=r_var, value=0,)

r2 = Radiobutton(text='Расшифровать',
                 variable=r_var, value=1)

r1.grid(column=3,row=0,pady=8, padx=8)
r2.grid(column=3,row=1,pady=8, padx=8)

def change():

    if r_var.get() == 0:
        btn_go.config(command=lambda: cripto(entrkey.get(), entr_txt.get()))
    elif r_var.get() == 1:
        btn_go.config(command=lambda: decripto(entrkey.get(), entr_txt.get()))

btn_save = Button(window, text="save",command= change)
btn_save.grid(column=4, row=0, pady=8, padx=8, sticky=E)

frame=LabelFrame(text='Вывод')
frame.grid(column=0,row=2,pady=8, padx=8,rowspan=2,columnspan=2)

text=Text(frame,width=30, height=5)
text.pack(side=LEFT)

frameTabl=LabelFrame(text='Таблица')
frameTabl.grid(column=2,row=2,rowspan=2,columnspan=2)

text2=Text(frameTabl,width=30, height=5)
text2.pack(side=LEFT)



window.mainloop()
