from tkinter import *
from tkinter import ttk
from datetime import datetime
from PIL import ImageTk
from tkvideo import tkvideo
import re
import ttkbootstrap as ttk
from ttkbootstrap.constants import *


# Глобальные переменные
coice = ''
temp = 0
after_id = ''


# Функции
def datatime(a):
    today = datetime.today()
    tlog = today.strftime("%Y-%m-%d|%H:%M:%S")
    tmain = today.strftime("%Y-%m-%d %H:%M:%S")
    if a: return tmain
    else: return tlog


def update_clock():
    today = datetime.today()
    t = today.strftime("%Y-%m-%d %H:%M:%S")
    labelInfo.configure(text=t)
    root.after(1000, update_clock)



def close():
    global win
    win.destroy()
    win.update()


def closeall():
    close()
    global win1
    win1.destroy()
    win1.update()


def click_cap():
    global coice
    global win
    coice = 'капучино'
    win = Toplevel()
    win.grab_set()
    win['bg'] = 'black'
    win.geometry('210x54+850+405')
    win.resizable(width=False, height=False)
    win.title('Подтверждение информации')
    lab = Label(win, text='Вы хотите приготовить капучино?', font=("Times New Roman", 10, "bold"))
    lab.pack(fill=X)
    btn_yes = Button(win, width=10, background='white', foreground='black', font=('Comic Sans MS', 13), compound=TOP,
                     text="Да", command=cook).place(x=0, y=21)
    btn_no = Button(win, background='white', foreground='black', font=('Comic Sans MS', 13), compound=TOP, text="Нет",
                    width=10, command=close).pack(anchor='e')


def click_ame():
    global coice
    global win
    coice = "американо"
    win = Toplevel()
    win.grab_set()
    win['bg'] = 'black'
    win.geometry('210x54+850+405')
    win.resizable(width=False, height=False)
    win.title('Подтверждение информации')
    l = Label(win, text='Вы хотите приготовить американо?', bg='red', font=("Times New Roman", 10, "bold")).pack(fill=X)
    btn_yes = Button(win, width=10, background='white', foreground='black', font=('Comic Sans MS', 13), compound=TOP,
                     text="Да", command=cook).place(x=0, y=21)
    btn_no = Button(win, background='white', foreground='black', font=('Comic Sans MS', 13), compound=TOP, text="Нет",
                    width=10, command=close).pack(anchor='e')


def click_lat():
    global coice
    global win
    coice = "латте"
    win = Toplevel()
    win.grab_set()
    win['bg'] = 'black'
    win.geometry('210x54+850+405')
    win.resizable(width=False, height=False)
    win.title('Подтверждение информации')
    l = Label(win, text='Вы хотите приготовить латте?', bg='red', font=("Times New Roman", 10, "bold")).pack(fill=X)
    btn_yes = Button(win, width=10, background='white', foreground='black', font=('Comic Sans MS', 13), compound=TOP,
                     text="Да", command=cook).place(x=0, y=21)
    btn_no = Button(win, background='white', foreground='black', font=('Comic Sans MS', 13), compound=TOP, text="Нет",
                    width=10, command=close).pack(anchor='e')


def click_de():
    global coice
    global win
    coice = "дв.эспрессо"
    win = Toplevel()
    win.grab_set()
    win['bg'] = 'black'
    win.geometry('210x54+850+405')
    win.resizable(width=False, height=False)
    win.title('Подтверждение информации')
    l = Label(win, text='Вы хотите приготовить дв.эспрессо?', bg='red', font=("Times New Roman", 10, "bold")).pack(fill=X)
    btn_yes = Button(win, width=10, background='white', foreground='black', font=('Comic Sans MS', 13), compound=TOP,
                     text="Да", command=cook).place(x=0, y=21)
    btn_no = Button(win, background='white', foreground='black', font=('Comic Sans MS', 13), compound=TOP, text="Нет",
                    width=10, command=close).pack(anchor='e')


def click_moc():
    global coice
    global win
    coice = "мокачино"
    win = Toplevel()
    win.grab_set()
    win['bg'] = 'black'
    win.geometry('210x54+850+405')
    win.resizable(width=False, height=False)
    win.title('Подтверждение информации')
    l = Label(win, width=20, text='Вы хотите приготовить мокачино?', bg='red', font=("Times New Roman", 10, "bold")).pack(fill=X)
    btn_yes = Button(win, width=10, background='white', foreground='black', font=('Comic Sans MS', 13), compound=TOP,
                     text="Да", command=cook).place(x=0, y=21)
    btn_no = Button(win, background='white', foreground='black', font=('Comic Sans MS', 13), compound=TOP, text="Нет",
                    width=10, command=close).pack(anchor='e')


def click_ex():
    global coice
    global win
    coice = "эспрессо"
    win = Toplevel()
    win.grab_set()
    win['bg'] = 'white'
    win.geometry('210x54+850+405')
    win.resizable(width=False, height=False)
    win.title('Подтверждение информации')
    l = Label(win, text='Вы хотите приготовить эспрессо?', bg='red', font=("Times New Roman", 10, "bold")).pack(fill=X)
    btn_yes = Button(win, width=10, background='white', foreground='black', font=('Comic Sans MS', 13), compound=TOP, text="Да", command=cook).place(x=0,y=21)
    btn_no = Button(win, background='white', foreground='black', font=('Comic Sans MS', 13), compound=TOP, text="Нет", width=10, command=close).pack(anchor='e')


def cook():
    def both():
        tick()
        start_vid()
    def tick():
        global temp, after_id
        stop = True
        after_id = win.after(50, tick)
        t = re.sub('\D', '', after_id)
        temp += 1
        lproc.configure(text=str(temp) + "%")
        lproc.pack(pady=5)
        if int(temp) == 100:
            temp = 0
            win.after_cancel(after_id)
            lvid.pack_forget()
            lready.pack(pady=5)
            btnClose.pack(pady=15)
            f = open('log/logs.txt', 'a', encoding='UTF-8')
            f.write(datatime(False) +' |' + coice.title() + '\n' )
            f.close()
    def start_vid():
        global lvid
        lvid = Label(win1, bg='white')
        lvid.pack()
        player = tkvideo('res/loading.mp4', lvid, loop=1, size=(150, 100))
        player.play()
    global coice
    global win1
    win1 = Toplevel()
    win1.grab_set()
    win1.overrideredirect(True)
    win1['bg'] = 'gray'
    win1.geometry('220x200+850+405')
    win1.resizable(width=False, height=False)
    win1.title('Приготовление')
    l = Label(win1, text='Идет процесс пригтовления ' + coice, bg='gray', font=("Times New Roman", 9, "bold")).pack(fill=X)
    lproc = Label(win1, text="0%", fg = 'white', bg='gray', font=("Times New Roman", 16, 'italic'))
    lready = Label(win1, text="Готово! \n Заберите ваш кофе", fg='gray', bg='black', font=("Times New Roman", 16, "bold"))
    btnClose = ttk.Button(win1, text="В главное меню", command=closeall)
    both()
    lproc.configure("0%")

# Логирование работы
file = open('log/logs.txt', 'a', encoding='UTF-8')
file.write('\nЗапуск кофемашины ' + datatime(False) + '\n')
file.write('___Дата___|__Время__|___Напиток____' + '\n' )
file.close()


#Наличие ингридиентов
file = op


# Параметры основного окна
root = Tk('minty')
root. title("Умная кофеварка")
root.geometry('720x720+600+200')
root.resizable(width=False, height=False)
root['bg'] = 'white'

# Изображения
imgEx = ImageTk.PhotoImage(file='res/Ecspresso.png')
imgCap = ImageTk.PhotoImage(file='res/Capuchino.png')
imgLat = ImageTk.PhotoImage(file='res/Latte.png')
imgDEx = ImageTk.PhotoImage(file='res/DoubleEcspresso.png')
imgAm = ImageTk.PhotoImage(file='res/Americano.png')
imgMoc = ImageTk.PhotoImage(file='res/Mocachino.png')
imgLogo = ImageTk.PhotoImage(file='res/Logo.png')

#Время
now = datetime.now()
formatted_date = str(now.strftime("%d.%m.%Y"))

# Стили ttk
styleLabels = ttk.Style()
styleLabels.configure('TLabel', background='#919191', fg='black', anchor=CENTER)
styleTop = ttk.Style()
styleTop.configure('TButton', background='white', foreground='black')
styleButtons = ttk.Style()
styleButtons.configure('TButton', font=('Comic Sans MS', 17), compound=TOP)




# Поля и кнопки главного окна
labelInfo = ttk.Label(root, anchor='n', font=("Cascadia", 11, "italic"))
labelInfo.pack(fill=BOTH)
labelLogo = ttk.Label(root, background='white', image=imgLogo).pack(anchor=CENTER, pady=20)
labelMain = ttk.Label(root, text='Выберите напиток', background='white', font='Calibri 35 bold').pack(padx=20, pady=0)
update_clock()


btnEcsp = ttk.Button(root, image=imgEx, text='Эспрессо', command=click_ex).place(x=40, y=300)
btnAmer = ttk.Button(root, image=imgAm, text='Американо', command=click_ame).place(x=40, y=510)
btnLat = ttk.Button(root, image=imgLat, text='Латте', command=click_lat).place(x=280, y=300)
btnDEcsp = ttk.Button(root, image=imgDEx, text='x2 Эспрессо',command=click_de).place(x=510, y=300)
btnMoc = ttk.Button(root, image=imgMoc, text='Мокачино', command=click_moc).place(x=280, y=510)
btnCapuch = ttk.Button(root, image=imgCap, text='Капучино', command=click_cap).place(x=510, y=510)




root.mainloop()
