# Импорт необходимых библиотек
from tkinter import *  # для GUI
from datetime import datetime  # для работы с датой/временем
from PIL import ImageTk  # для работы с изображениями
from tkvideo import tkvideo  # для воспроизведения видео в tkinter
import ttkbootstrap as ttk  # стилизованные виджеты
from pathlib import Path  # для работы с путями файлов
import hashlib  # для хеширования паролей


# Глобальные переменные
coice = ''  # выбранный напиток
temp = 0  # временная переменная для прогресса приготовления
after_id = ''  # ID для отмены анимации прогресса


# Функции
def datatime(a):
    """Форматирование даты/времени для логов или интерфейса"""
    today = datetime.today()
    tlog = today.strftime("%Y-%m-%d|%H:%M:%S")  # формат для логов
    tmain = today.strftime("%Y-%m-%d %H:%M:%S")  # формат для интерфейса
    if a: return tmain
    else: return tlog


def update_clock():
    """Обновление времени в интерфейсе"""
    today = datetime.today()
    t = today.strftime("%Y-%m-%d %H:%M:%S")
    labelInfo.configure(text=t)
    root.after(1000, update_clock)  # рекурсивный вызов каждую секунду


def close():
    """Закрытие окна подтверждения"""
    global win
    win.destroy()
    win.update()


def closeall():
    """Закрытие всех окон"""
    close()
    global win1
    win1.destroy()
    win1.update()


# Функции для каждого типа кофе (аналогичная структура)
def click_cap():
    """Обработка выбора капучино"""
    ingr = latest_start()  # получение текущих ингредиентов
    # Проверка достаточности ингредиентов
    if int(ingr[0]) < recepie.cofcap or int(ingr[1]) < recepie.mcap or int(ingr[2]) < recepie.crcap or int(ingr[3]) < recepie.wcap:
        # Создание окна с ошибкой
        win1 = Toplevel()
        win1.grab_set()
        win1['bg'] = 'white'
        win1.geometry('210x54+850+405')
        win1.resizable(width=False, height=False)
        win1.title('Нет ингридиентов')
        label = Label(win1, text='В кофемашине \nнедостаточно ингридиентов!', background='red',
                      font=("Times New Roman", 10, "bold")).pack(fill=X)
    else:
        # Если ингредиентов достаточно
        global coice
        global win
        coice = 'капучино'
        # Создание окна подтверждения
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
        minus_ingr(recepie.cofcap, recepie.mcap, recepie.crcap, recepie.wcap)  # вычитание ингредиентов


# Аналогичные функции для других видов кофе (click_ame, click_lat, click_de, click_moc, click_ex)


def cook():
    """Процесс приготовления кофе"""
    def both():
        """Запуск анимации и прогресс-бара"""
        tick()
        start_vid()
        
    def tick():
        """Обновление прогресс-бара"""
        global temp, after_id
        after_id = win1.after(10, tick)  # обновление каждые 10 мс
        temp += 1
        lproc.configure(text=str(temp) + "%")
        lproc.pack(pady=5)
        if int(temp) == 100:
            temp = 0
            win1.after_cancel(after_id)
            lvid.pack_forget()
            lready.pack(pady=5)
            btnClose.pack(pady=15)
            # Запись в лог
            f = open('log/logs.txt', 'a', encoding='UTF-8')
            f.write(datatime(False) +' |' + coice.title() + '\n' )
            f.close()
            
    def start_vid():
        """Запуск анимации приготовления"""
        global lvid
        lvid = Label(win1, bg='white')
        lvid.pack()
        player = tkvideo('res/loading.mp4', lvid, loop=1, size=(150, 100))
        player.play()
        
    global coice
    global win1
    # Создание окна приготовления
    win1 = Toplevel()
    win1.grab_set()
    win1.overrideredirect(True)  # окно без рамки
    win1['bg'] = 'gray'
    win1.geometry('220x200+850+405')
    win1.resizable(width=False, height=False)
    win1.title('Приготовление')
    l = Label(win1, text='Идет процесс пригтовления ' + coice, bg='gray', font=("Times New Roman", 9, "bold")).pack(fill=X)
    lproc = Label(win1, text="0%", fg = 'white', bg='gray', font=("Times New Roman", 16, 'italic'))
    lready = Label(win1, text="Готово! \n Заберите ваш кофе", fg='gray', bg='black', font=("Times New Roman", 16, "bold"))
    btnClose = ttk.Button(win1, text="В главное меню", command=closeall)
    both()  # запуск процесса


def start_cfg():
    """Инициализация файла конфигурации"""
    with open('cfg/ingr.txt', 'w', encoding='UTF-8') as file:
                file.write ('0 0 0 0')


def latest_start():
    """Получение текущего состояния ингредиентов"""
    # cfg[1] - coffee
    # cfg[2] - milk
    # cfg[3] - cream
    # cfg[4] - water
    with open('cfg/ingr.txt', 'r', encoding='UTF-8') as file:
        cfg = list(file.read().split(" "))
        return cfg


def minus_ingr(coffee, milk, cream, water):
    """Вычитание использованных ингредиентов"""
    cfg = latest_start()
    newcfg = str([int(cfg[0])-coffee,int(cfg[1]) - milk, int(cfg[2]) - cream, int(cfg[3]) - water])
    with open('cfg/ingr.txt', 'w', encoding='UTF-8') as file:
        new = ''
        for i in newcfg:
            if i != '[' and i != ']' and i != ',':
                new = new + i
        file.write(new)


def set_config():
    """Установка новых значений ингредиентов"""
    def confirm_cfg():
        """Подтверждение новых значений"""
        coffee = str(coffeePlace.get())
        milk = str(milkPlace.get())
        cream = str(creamPlace.get())
        water = str(waterPlace.get())
        with open('cfg/ingr.txt', 'w', encoding='UTF-8') as file:
            file.write(coffee + ' ' + milk + ' ' + cream + ' ' + water)
        win3.destroy()
        
    # Создание окна настроек
    win3 = Toplevel()
    win3.grab_set()
    win3['bg'] = 'gray'
    win3.geometry('250x200+850+405')
    win3.resizable(width=False, height=False)
    win3.title('Смена конфигурации')
    # Поля ввода для каждого ингредиента
    labelCoffee = ttk.Label(win3, text="Кофе:", background="gray", foreground='black', font=("Times New Roman", 12, 'bold'))
    labelCoffee.pack(pady=9, padx=7, anchor='w')
    # ... аналогичные поля для других ингредиентов
    btnConfirm = Button(win3, text='Подтвердить', font=('Times New Roman', 11), width=13, bg='white', fg='black', command=confirm_cfg)
    btnConfirm.pack(pady=8)


def admin():
    """Аутентификация администратора"""
    def confirm():
        """Проверка пароля"""
        pw = password_place.get()
        hash_password = str(hashlib.sha256(pw.encode()).hexdigest())

        with open('cfg/pw.txt', 'r') as password:
            pas = password.read()
            if hash_password == pas:
                set_config()  # если пароль верный
                win2.destroy()
            else:
                label['text'] = 'Неверный пароль'

    def change_password():
        """Смена пароля администратора"""
        win2.destroy()
        def try_pass():
            """Попытка смены пароля"""
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

        # Окно смены пароля
        win4 = Toplevel()
        win4.grab_set()
        win4['bg'] = 'gray'
        win4.geometry('250x150+850+405')
        win4.resizable(width=False, height=False)
        win4.title('Смена пароля')
        # Поля для старого и нового пароля
        oldPassPlace = ttk.Entry(win4, width=17, show='*')
        oldPassPlace.place(x=125, y=5)
        newPassPlace = ttk.Entry(win4, width=17, show='*')
        newPassPlace.place(x=125, y=45)
        # ... остальные элементы интерфейса

    # Окно аутентификации
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
    """Класс с рецептами напитков (количество ингредиентов)"""
    cofcap = 7  # кофе для капучино
    cofame = 8  # кофе для американо
    # ... остальные рецепты


# Инициализация файла конфигурации, если он пустой
mypath = Path('cfg/ingr.txt')
if mypath.stat().st_size == 0:
    start_cfg()


# Логирование запуска
file = open('log/logs.txt', 'a', encoding='UTF-8')
file.write('\nЗапуск кофемашины ' + datatime(False) + '\n')
file.write('___Дата___|__Время__|___Напиток____' + '\n' )
file.close()


# Основное окно
root = Tk('minty')
root. title("Умная кофеварка")
root.geometry('720x720+500+50')
root.resizable(width=False, height=False)
root['bg'] = 'white'

# Загрузка изображений для кнопок
imgEx = ImageTk.PhotoImage(file='res/Ecspresso.png')
imgCap = ImageTk.PhotoImage(file='res/Capuchino.png')
# ... остальные изображения

# Текущая дата
now = datetime.now()
formatted_date = str(now.strftime("%d.%m.%Y"))

# Настройка стилей
styleLabels = ttk.Style()
styleLabels.configure('TLabel', background='#919191', fg='black', anchor=CENTER)
styleTop = ttk.Style()
styleTop.configure('TButton', background='white', foreground='black')
styleButtons = ttk.Style()
styleButtons.configure('TButton', font=('Comic Sans MS', 17), compound=TOP)


# Создание элементов интерфейса
labelInfo = ttk.Label(root, anchor='n', font=("Cascadia", 11, "italic"))
labelInfo.pack(fill=BOTH)
labelLogo = ttk.Label(root, background='white', image=imgLogo).pack(anchor=CENTER, pady=20)
labelMain = ttk.Label(root, text='Выберите напиток', background='white', font='Calibri 35 bold').pack(padx=20, pady=0)
update_clock()  # запуск обновления времени

# Кнопки напитков
btnCfg = Button(root, text='Задать параметры конфигурации', font=('Times New Roman', 9), bg = 'white', fg = 'black', command=admin)
btnCfg.place(x=514, y=685)
btnEcsp = ttk.Button(root, image=imgEx, text='Эспрессо', command=click_ex).place(x=40, y=260)
# ... остальные кнопки напитков

root.mainloop()  # запуск основного цикла
