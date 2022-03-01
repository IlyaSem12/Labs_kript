from tkinter import *
from tkinter import messagebox as mb
window = Tk()
window.title("Шифр цезаря")
window.resizable(False,False)

alf = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'


def cripto():
    word = entr_txt.get().upper()
    try:
        step = int(entrstep.get())
    except:
        mb.showerror(
            "Ошибка",
            "Должно быть введено число")

    message = ""
    revmessage = ""

    for i in word:
        place = alf.find(i)
        new_place = place + step
        if i in alf:
            message += alf[new_place]
        else:
            message += i

    for i in message:
        place = alf.find(i)
        new_place = place - step
        if i in alf:
            revmessage += alf[new_place]
        else:
            revmessage += i

    print(message)
    print(revmessage)
    text.insert(1.0, message + '\n')
    text.insert(2.0, revmessage + '\n')


lbl= Label(window,text="Введите слово:").grid(column=0,row=0,pady=8, padx=8)
lbl2= Label(window,text="Введите шаг:").grid(column=0,row=1,pady=8, padx=8,sticky=W)


entr_txt=Entry(window,width=30)
entr_txt.grid(column=1,row=0,columnspan=3,pady=8, padx=8)
entrstep=Entry(window,width=15)
entrstep.grid(column=1,row=1,pady=8, padx=8,sticky=W)


btn_go = Button(window,text="Пуск",command=cripto).grid(column=2,row=1,pady=8, padx=8,sticky=W)


frame=LabelFrame(text='Вывод')
frame.grid(column=4,row=0,pady=8, padx=8,rowspan=2,columnspan=2)

text=Text(frame,width=30, height=5)
text.pack(side=LEFT)




window.mainloop()
