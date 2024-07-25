from tkinter import *
from datetime import datetime
from PIL import ImageTk
from tkvideo import tkvideo
import ttkbootstrap as ttk
from pathlib import Path
import hashlib


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
    ingr = latest_start()
    if int(ingr[0]) < recepie.cofcap or int(ingr[1]) < recepie.mcap or int(ingr[2]) < recepie.crcap or int(
            ingr[3]) < recepie.wcap:
        win1 = Toplevel()
        win1.grab_set()
        win1['bg'] = 'white'
        win1.geometry('210x54+850+405')
        win1.resizable(width=False, height=False)
        win1.title('Нет ингридиентов')
        label = Label(win1, text='В кофемашине \nнедостаточно ингридиентов!', background='red',
                      font=("Times New Roman", 10, "bold")).pack(fill=X)
    else:
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
        btn_yes = Button(win, width=10, background='white', foreground='black', font=('Comic Sans MS', 13),
                         text="Да", command=cook).place(x=0, y=21)
        btn_no = Button(win, background='white', foreground='black', font=('Comic Sans MS', 13),  text="Нет",
                        width=10, command=close).pack(anchor='e')
        minus_ingr(recepie.cofcap, recepie.mcap, recepie.crcap, recepie.wcap)


def click_ame():
    ingr = latest_start()
    if int(ingr[0]) < recepie.cofame or int(ingr[1]) < recepie.mame or int(ingr[2]) < recepie.crame or int(
            ingr[3]) < recepie.wame:
        win1 = Toplevel()
        win1.grab_set()
        win1['bg'] = 'white'
        win1.geometry('210x54+850+405')
        win1.resizable(width=False, height=False)
        win1.title('Нет ингридиентов')
        label = Label(win1, text='В кофемашине \nнедостаточно ингридиентов!', background='red',
                      font=("Times New Roman", 10, "bold")).pack(fill=X)
    else:
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
        btn_yes = Button(win, width=10, background='white', foreground='black', font=('Comic Sans MS', 13),
                         text="Да", command=cook).place(x=0, y=21)
        btn_no = Button(win, background='white', foreground='black', font=('Comic Sans MS', 13), text="Нет",
                        width=10, command=close).pack(anchor='e')
        minus_ingr(recepie.cofame, recepie.mame, recepie.crame, recepie.wame)


def click_lat():
    ingr = latest_start()
    if int(ingr[0]) < recepie.coflat or int(ingr[1]) < recepie.mlat or int(ingr[2]) < recepie.crlat or int(
            ingr[3]) < recepie.wlat:
        win1 = Toplevel()
        win1.grab_set()
        win1['bg'] = 'white'
        win1.geometry('210x54+850+405')
        win1.resizable(width=False, height=False)
        win1.title('Нет ингридиентов')
        label = Label(win1, text='В кофемашине \nнедостаточно ингридиентов!', background='red',
                      font=("Times New Roman", 10, "bold")).pack(fill=X)
    else:
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
        btn_yes = Button(win, width=10, background='white', foreground='black', font=('Comic Sans MS', 13),
                         text="Да", command=cook).place(x=0, y=21)
        btn_no = Button(win, background='white', foreground='black', font=('Comic Sans MS', 13), text="Нет",
                        width=10, command=close).pack(anchor='e')
        minus_ingr(recepie.coflat, recepie.mlat, recepie.crlat, recepie.wlat)


def click_de():
    ingr = latest_start()
    if int(ingr[0]) < recepie.cofdex or int(ingr[1]) < recepie.mdex or int(ingr[2]) < recepie.crdex or int(
            ingr[3]) < recepie.wdex:
        win1 = Toplevel()
        win1.grab_set()
        win1['bg'] = 'white'
        win1.geometry('210x54+850+405')
        win1.resizable(width=False, height=False)
        win1.title('Нет ингридиентов')
        label = Label(win1, text='В кофемашине \nнедостаточно ингридиентов!', background='red',
                      font=("Times New Roman", 10, "bold")).pack(fill=X)
    else:
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
        btn_yes = Button(win, width=10, background='white', foreground='black', font=('Comic Sans MS', 13),
                         text="Да", command=cook).place(x=0, y=21)
        btn_no = Button(win, background='white', foreground='black', font=('Comic Sans MS', 13), text="Нет",
                        width=10, command=close).pack(anchor='e')
        minus_ingr(recepie.cofdex, recepie.mdex, recepie.crdex, recepie.wdex)


def click_moc():
    ingr = latest_start()
    if int(ingr[0]) < recepie.cofmo or int(ingr[1]) < recepie.mmo or int(ingr[2]) < recepie.crmo or int(
            ingr[3]) < recepie.wmo:
        win1 = Toplevel()
        win1.grab_set()
        win1['bg'] = 'white'
        win1.geometry('210x54+850+405')
        win1.resizable(width=False, height=False)
        win1.title('Нет ингридиентов')
        label = Label(win1, text='В кофемашине \nнедостаточно ингридиентов!', background='red',
                      font=("Times New Roman", 10, "bold")).pack(fill=X)
    else:
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
        btn_yes = Button(win, width=10, background='white', foreground='black', font=('Comic Sans MS', 13),
                         text="Да", command=cook).place(x=0, y=21)
        btn_no = Button(win, background='white', foreground='black', font=('Comic Sans MS', 13),  text="Нет",
                        width=10, command=close).pack(anchor='e')
        minus_ingr(recepie.cofmo, recepie.mmo, recepie.crmo, recepie.wmo)


def click_ex():
    ingr = latest_start()
    if int(ingr[0]) < recepie.cofex or int(ingr[1]) < recepie.mex or int(ingr[2]) < recepie.crex or int(ingr[3]) < recepie.wex:
        win1 = Toplevel()
        win1.grab_set()
        win1['bg'] = 'white'
        win1.geometry('210x54+850+405')
        win1.resizable(width=False, height=False)
        win1.title('Нет ингридиентов')
        label = Label(win1, text='В кофемашине \nнедостаточно ингридиентов!', background='red', font=("Times New Roman", 10, "bold")).pack(fill=X)
    else:
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
        btn_yes = Button(win, width=10, background='white', foreground='black', font=('Comic Sans MS', 13), text="Да", command=cook).place(x=0,y=21)
        btn_no = Button(win, background='white', foreground='black', font=('Comic Sans MS', 13), text="Нет", width=10, command=close).pack(anchor='e')
        minus_ingr(recepie.cofex, recepie.mex, recepie.crex, recepie.wex)

def cook():
    def both():
        tick()
        start_vid()
    def tick():
        global temp, after_id
        after_id = win1.after(10, tick)
        temp += 1
        lproc.configure(text=str(temp) + "%")
        lproc.pack(pady=5)
        if int(temp) == 100:
            temp = 0
            win1.after_cancel(after_id)
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



def start_cfg():
    with open('cfg/ingr.txt', 'w', encoding='UTF-8') as file:
                file.write ('0 0 0 0')



def latest_start():
    # cfg[1] - coffee
    # cfg[2] - milk
    # cfg[3] - cream
    # cfg[4] - water
    with open('cfg/ingr.txt', 'r', encoding='UTF-8') as file:
        cfg = list(file.read().split(" "))
        return cfg


def minus_ingr(coffee, milk, cream, water):
    cfg = latest_start()
    newcfg = str([int(cfg[0])-coffee,int(cfg[1]) - milk, int(cfg[2]) - cream, int(cfg[3]) - water])
    with open('cfg/ingr.txt', 'w', encoding='UTF-8') as file:
        new = ''
        for i in newcfg:
            if i != '[' and i != ']' and i != ',':
                new = new + i
        file.write(new)


def set_config():
    def confirm_cfg():
        coffee = str(coffeePlace.get())
        milk = str(milkPlace.get())
        cream = str(creamPlace.get())
        water = str(waterPlace.get())
        with open('cfg/ingr.txt', 'w', encoding='UTF-8') as file:
            file.write(coffee + ' ' + milk + ' ' + cream + ' ' + water)
        win3.destroy()
    win3 = Toplevel()
    win3.grab_set()
    win3['bg'] = 'gray'
    win3.geometry('250x200+850+405')
    win3.resizable(width=False, height=False)
    win3.title('Смена конфигурации')
    labelCoffee = ttk.Label(win3, text="Кофе:", background="gray", foreground='black', font=("Times New Roman", 12, 'bold'))
    labelCoffee.pack(pady=9, padx=7, anchor='w')
    labelMilk = ttk.Label(win3, text="Молоко:", background="gray",foreground='black', font=("Times New Roman", 12, 'bold'))
    labelMilk.pack(pady=7, padx=7, anchor='w')
    labelCream = ttk.Label(win3, text="Сливки:", background="gray",foreground='black', font=("Times New Roman", 12, 'bold'))
    labelCream.pack(pady=8, padx=7, anchor='w')
    labelWater = ttk.Label(win3, text="Вода:", background="gray",foreground='black', font=("Times New Roman", 12, 'bold'))
    labelWater.pack(pady=8, padx=7, anchor='w')
    coffeePlace = ttk.Entry(win3)
    coffeePlace.place(x=100, y=5)
    milkPlace = ttk.Entry(win3)
    milkPlace.place(x=100, y=45)
    creamPlace = ttk.Entry(win3)
    creamPlace.place(x=100, y=85)
    waterPlace = ttk.Entry(win3)
    waterPlace.place(x=100, y=125)
    btnConfirm = Button(win3, text='Подтвердить', font=('Times New Roman', 11), width=13, bg='white', fg='black', command=confirm_cfg)
    btnConfirm.pack(pady=8)



def admin():
    def confirm():
        pw = password_place.get()
        hash_password = str(hashlib.sha256(pw.encode()).hexdigest())

        with open('cfg/pw.txt', 'r') as password:
            pas = password.read()
            if hash_password == pas:
                set_config()
                win2.destroy()
            else:
                label['text'] = 'Неверный пароль'


    def change_password():
        win2.destroy()
        def try_pass():
            oldpw = oldPassPlace.get()
            hash_oldpasswordd = str(hashlib.sha256(oldpw.encode()).hexdigest())
            newpw = newPassPlace.get()
            hash_newpasswordd = str(hashlib.sha256(newpw.encode()).hexdigest())
            with open('cfg/pw.txt', 'r') as pw:
                passw = pw.read()
            if passw == hash_oldpasswordd:
                with open('cfg/pw.txt', 'w') as changepw:
                    changepw.write(hash_newpasswordd)
                    win4.destroy()
            else:
                labelConfirm['text'] = 'Неверный старый пароль'


        win4 = Toplevel()
        win4.grab_set()
        win4['bg'] = 'gray'
        win4.geometry('250x150+850+405')
        win4.resizable(width=False, height=False)
        win4.title('Смена пароля')
        oldPassPlace = ttk.Entry(win4, width=17, show='*')
        oldPassPlace.place(x=125, y=5)
        newPassPlace = ttk.Entry(win4, width=17, show='*')
        newPassPlace.place(x=125, y=45)
        labelOldPass = ttk.Label(win4, text="Старый пароль:", background="gray", foreground='black', font=("Times New Roman", 11, 'bold'))
        labelOldPass.pack(pady=9, padx=7, anchor='w')
        labelNewPass = ttk.Label(win4, text="Новый пароль:", background="gray", foreground='black', font=("Times New Roman", 11, 'bold'))
        labelNewPass.pack(pady=7, padx=7, anchor='w')
        labelConfirm = ttk.Label(win4, background='gray', text='Заполните поля', font=("Times New Roman", 11, 'bold'))
        labelConfirm.pack(anchor='n', pady=7)
        btnConfirm = Button(win4, text='Подтвердить', font=('Times New Roman', 11), width=13, bg='white', fg='black', command=try_pass)
        btnConfirm.pack(anchor='n')


    win2 = Toplevel()
    win2.grab_set()
    win2['bg'] = 'gray'
    win2.geometry('250x100+850+405')
    win2.resizable(width=False, height=False)
    win2.title('Значения конфигурации')
    label = ttk.Label(win2, text="Введите пароль администратора:")
    password_place = ttk.Entry(win2, show='*')
    btn_enter_pass = Button(win2, text='Подтвердить', font=('Times New Roman', 11), width=13, bg='white', fg='black', command=confirm)
    btn_change_pass = Button(win2, text='Сменить пароль', font=('Times New Roman', 11),width=13, bg='white', fg='black', command=change_password)
    label.pack()
    password_place.pack(padx=4, pady=9)
    btn_enter_pass.place(x=130, y=65)
    btn_change_pass.place(x=10, y=65)




class recepie:
    cofcap = 7
    cofame = 8
    coflat = 7
    cofex = 8
    cofdex = 8
    cofmo = 8
    mcap = 270
    mame = 0
    mlat = 135
    mex = 0
    mdex = 8
    mmo = 165
    wcap = 30
    wame = 300
    wlat = 30
    wex = 30
    wdex = 60
    wmo = 0
    crcap = 0
    crame = 0
    crlat = 135
    crex = 0
    crdex = 0
    crmo = 105


mypath = Path('cfg/ingr.txt')
if mypath.stat().st_size == 0:
    start_cfg()


# Логирование работы
file = open('log/logs.txt', 'a', encoding='UTF-8')
file.write('\nЗапуск кофемашины ' + datatime(False) + '\n')
file.write('___Дата___|__Время__|___Напиток____' + '\n' )
file.close()


# Параметры основного окна
root = Tk('minty')
root. title("Умная кофеварка")
root.geometry('720x720+500+50')
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

btnCfg = Button(root, text='Задать параметры конфигурации', font=('Times New Roman', 9), bg = 'white', fg = 'black', command=admin)
btnCfg.place(x=514, y=685)
btnEcsp = ttk.Button(root, image=imgEx, text='Эспрессо', command=click_ex).place(x=40, y=260)
btnAmer = ttk.Button(root, image=imgAm, text='Американо', command=click_ame).place(x=40, y=470)
btnLat = ttk.Button(root, image=imgLat, text='Латте', command=click_lat).place(x=280, y=260)
btnDEcsp = ttk.Button(root, image=imgDEx, text='x2 Эспрессо',command=click_de).place(x=510, y=260)
btnMoc = ttk.Button(root, image=imgMoc, text='Мокачино', command=click_moc).place(x=280, y=470)
btnCapuch = ttk.Button(root, image=imgCap, text='Капучино', command=click_cap).place(x=510, y=470)




root.mainloop()