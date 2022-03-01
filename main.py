from tkinter import *

window = Tk()
window.title("Шифр цезаря")
window.geometry('600x500')

alf = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'



word = input('Введите слово:').upper()
step = int(input('Введите шаг:'))

revmessage = ""

for i in word:
    place = alf.find(i)
    new_place = place + step
    if i in alf:
        revmessage += alf[new_place]
    else:
        revmessage += i


print(revmessage)


labl1 = Label(window,text="Введите слово:")
labl1.grid(row=2,column=0)


window.mainloop()