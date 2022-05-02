import pandas as pd
from prettytable import PrettyTable
lst = input("Введите текст:").lower()
print(lst)
mytable = PrettyTable()
mytable.field_names = ["сдвиг","Кол-во совпадений","доля"]


doli= []
mass = []
mass.append(lst)

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

    return (res)


def similarity(s1, s2):# кол-во совподающих букв
  normalized1 = s1.lower()
  normalized2 = s2.lower()

  count = 0
  for i,t in enumerate(normalized1):

      if t == normalized2[i]:

        count +=1

      else:
          k = 0
  return count


def check_freq(str): # частота появления букв
    freq = {}
    for c in str:
       freq[c] = str.count(c)
    return freq

def get_key(d, value):# берём ключ по значению
    for k, v in d.items():
        if v == value:
            return k


for i in range(15):#сдвиг текста
    n = i+1
    step = (lst[n:] +lst[:n]).strip()
    mass.append(step)
    # print(i+1,' ',mass,'\n')


for i in range(len(mass)): #заполнение таблицы
    txt = mass[0]
    if (i + 1) < len(mass):
        message = mass[i + 1]
        print(message)
        s = similarity(txt, message)
        dol = s/len(mass[0])
        doli.append(dol)
        mytable.add_row([i+1,s,dol])

max_num = max(doli)
l=0
print(mytable)
for i in range(len(doli)):
    if max_num == doli[i]:
        l = i+1

print(l, '', max_num)

k=[]
words=[]
chunks = [mass[0][i:i+l] for i in range(0, len(mass[0]), l)]#делим по l букв
print(chunks)

for i in range(l):
    k.append([])
    words.append([])

j=0
tmp=[]
for i in range(len(chunks)): #разбиваем буквы по k
    tmp.append(chunks[i])

    while j<len(tmp[0]):
        k[j].append(tmp[0][j])
        j+=1
    tmp.clear()
    j=0

print(k)



for i in range(len(k)):
    tmp.append([])
    print('k',i+1)
    print(pd.Series(list(k[i])).value_counts())
    print('-----')
    tmp[i].append(check_freq("".join(k[i])))

print(tmp)


for i in range(len(tmp)):
    for p in range(len(tmp[i])):
        words[i].append(get_key(tmp[i][p],max(tmp[i][p].values())))
        print(max(tmp[i][p].values()))
        print('-----')

print(words)

key = []

for i in range(len(words)):
    key.append(decodevi('о',words[i][j]))

print(decodevi("".join(key),lst))