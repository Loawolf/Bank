from tkinter import *
from tkinter import messagebox
import matplotlib.pyplot as plt
from PIL import Image, ImageTk
import requests

root = Tk()
root.config(background='#F2F2F2')
root.title('Московский Кредитный Банк МКБ')
root.iconbitmap(r'Mkb.ico')

# Проверка регистрации
log = False
pas = False

# Добавление картинок
s1 = Image.open("pic/iarkiI.png")
p1 = ImageTk.PhotoImage(s1)

s2 = Image.open("pic/Nakop.png")
p2 = ImageTk.PhotoImage(s2)

s3 = Image.open("pic/Vse_VKL.png")
p3 = ImageTk.PhotoImage(s3)

r1 = Image.open("pic/time.png")
c1 = ImageTk.PhotoImage(r1)

r2 = Image.open("pic/goal.png")
c2 = ImageTk.PhotoImage(r2)

r3 = Image.open("pic/calc.png")
c3 = ImageTk.PhotoImage(r3)

log_im = Image.open("pic/Screenshot_8.png")
test = ImageTk.PhotoImage(log_im)


class instrac():
    def depos():
        dep = Toplevel()
        dep.title('Инструкция к депозитам')
        dep.iconbitmap(r'Mkb.ico')
    # Тариф Яркий
        Label(dep, text=f'МКБ. Яркий', font='Arial 13 bold').grid(
            row=0, column=1, columnspan=2)
        Label(dep, text=f'10,5%', foreground='red', font='Arial 13 bold').grid(
            row=0, column=0)
        Label(dep, image=p1).grid(
            row=1, column=0)
        Label(dep, text='Условия:\n Ставка до 10,5% \n Сумма до 3 млн. ₽ \n Доход 158 219 ₽').grid(
            row=1, column=1)
        Button(dep, text='Оформить\n заявку', bg='#D9042B', font='Arial 10 bold', width=10,
               foreground='white', command=url1).grid(row=1, column=2)
    # Отступы
        Label().grid(row=2, column=0)
        Label().grid(row=2, column=1)
        Label().grid(row=2, column=2)
    # Тариф Накопительный
        Label(dep, text=f'Накопительный счет', font='Arial 13 bold').grid(
            row=3, column=1, columnspan=2)
        Label(dep, text=f'10%', foreground='red', font='Arial 13 bold').grid(
            row=3, column=0)
        Label(dep, image=p2).grid(
            row=4, column=0)
        Label(dep, text='Условия:\n Ставка до 10% \n Сумма до 1 млн 500 тыс. ₽ \n Доход 150 685 ₽').grid(
            row=4, column=1)
        Button(dep, text='Оформить\n заявку', bg='#D9042B', font='Arial 10 bold', width=10,
               foreground='white', command=url1).grid(row=4, column=2)
    # Отступы
        Label().grid(row=5, column=0)
        Label().grid(row=5, column=1)
        Label().grid(row=5, column=2)
    # Тариф Все включено
        Label(dep, text=f'Все включено', font='Arial 13 bold').grid(
            row=6, column=1, columnspan=2)
        Label(dep, text=f'9,5%', foreground='red', font='Arial 13 bold').grid(
            row=6, column=0)
        Label(dep, image=p3).grid(
            row=7, column=0)
        Label(dep, text='Условия:\n Ставка до 9,5% \n Сумма до 20 млн ₽ \n Доход до 143 151 ₽').grid(
            row=7, column=1)
        Button(dep, text='Оформить\n заявку', bg='#D9042B', font='Arial 10 bold', width=10,
               foreground='white', command=url1).grid(row=7, column=2)

    def credit():
        cred = Toplevel()
        cred.title('Инструкция к Кредитам')
        cred.iconbitmap(r'Mkb.ico')
    # Тариф Время возможностей
        Label(cred, text=f'Акция «Время возможностей»', font='Arial 13 bold').grid(
            row=0, column=1, columnspan=2)
        Label(cred, text=f'9,9%', foreground='red', font='Arial 13 bold').grid(
            row=0, column=0)
        Label(cred, image=c1).grid(
            row=1, column=0)
        Label(cred, text='Условия:\n Ставка от 9,9% \n Сумма до 5 млн. ₽ \n Ежемесячный платеж 24 165 ₽').grid(
            row=1, column=1)
        Button(cred, text='Оформить\n заявку', bg='#D9042B', font='Arial 10 bold', width=10,
               foreground='white', command=url2).grid(row=1, column=2)
    # Отступы
        Label().grid(row=2, column=0)
        Label().grid(row=2, column=1)
        Label().grid(row=2, column=2)
    # Тариф На любые цели
        Label(cred, text=f'Кредит на любые цели', font='Arial 13 bold').grid(
            row=3, column=1, columnspan=2)
        Label(cred, text=f'9,9%', foreground='red', font='Arial 13 bold').grid(
            row=3, column=0)
        Label(cred, image=c2).grid(
            row=4, column=0)
        Label(cred, text='Условия:\n Ставка от 9,9% \n Сумма до 5 млн ₽ \n Ежемесячный платеж 24 165 ₽').grid(
            row=4, column=1)
        Button(cred, text='Оформить\n заявку', bg='#D9042B', font='Arial 10 bold', width=10,
               foreground='white', command=url2).grid(row=4, column=2)
    # Отступы
        Label().grid(row=5, column=0)
        Label().grid(row=5, column=1)
        Label().grid(row=5, column=2)

    # Тариф Рефинансирование кредитов
        Label(cred, text=f'Рефинансирование кредитов', font='Arial 13 bold').grid(
            row=6, column=1, columnspan=2)
        Label(cred, text=f'9,9%', foreground='red', font='Arial 13 bold').grid(
            row=6, column=0)
        Label(cred, image=c3).grid(
            row=7, column=0)
        Label(cred, text='Условия:\n Ставка от 9,9% \n Сумма до 5 млн ₽ \n Ежемесячный платеж до 24 165 ₽').grid(
            row=7, column=1)
        Button(cred, text='Оформить\n заявку', bg='#D9042B', font='Arial 10 bold', width=10,
               foreground='white', command=url2).grid(row=7, column=2)

    def rasch():
        def calculate_credit():
            try:
                float(principal_entry.get())
                float(interest_rate_entry.get())
                float(time_period_entry.get())
            except:
                messagebox.showerror(
                    'Ошибка ввода', "Введите во все поля данные!\nИ указывайте их корректно!")
                window.destroy()

            principal = float(principal_entry.get())
            interest_rate = float(interest_rate_entry.get())
            time_period = float(time_period_entry.get())

            total_amount = principal * (1 + interest_rate / 100) ** time_period

            monthly_payment = total_amount / (12 * time_period)

            messagebox.showinfo(
                "Результаты расчета",
                f"Вы будете должны в общем: {total_amount:.2f} рублей\n\n"
                f"Ежемесячный платеж составит: {monthly_payment:.2f} рублей",
            )

        def calculate_deposit():
            try:
                float(principal_entry.get())
                float(interest_rate_entry.get())
                float(time_period_entry.get())
            except:
                messagebox.showerror(
                    'Ошибка ввода', "Введите во все поля данные!\nИ указывайте их корректно!")
                window.destroy()

            principal = float(principal_entry.get())
            interest_rate = float(interest_rate_entry.get())
            time_period = float(time_period_entry.get())

            total_amount = principal * (1 + interest_rate / 100) ** time_period

            monthly_payment = total_amount / time_period

            messagebox.showinfo("Результаты расчета", f"Итого будет: {total_amount:.2f} рублей\n\n"
                                f"Ежегодные выплаты составят: {monthly_payment:.2f} рублей")

        def on_calculation_type_selected():
            selected_calculation_type = calculation_type.get()
            if selected_calculation_type == "Рассчитать кредит":
                calculate_credit()
            elif selected_calculation_type == "Рассчитать депозит":
                calculate_deposit()
            elif selected_calculation_type == "Выберите тип расчета":
                messagebox.showerror(
                    "Ошибка", 'Сначала нужно выбрать тип расчета!')

        def generate_payment_schedule():
            try:
                float(principal_entry.get())
                float(interest_rate_entry.get())
                float(time_period_entry.get())
            except:
                messagebox.showerror(
                    'Ошибка ввода', "Введите во все поля данные!\nИ указывайте их корректно!")
                window.destroy()

            principal = int(principal_entry.get())
            interest_rate = float(interest_rate_entry.get())
            years = int(time_period_entry.get())

            # Расчет ежемесячного платежа
            monthly_interest_rate = interest_rate / 100 / 12
            months = years * 12
            monthly_payment = principal * (monthly_interest_rate * (
                1 + monthly_interest_rate) ** months) / ((1 + monthly_interest_rate) ** months - 1)

            # Создание графика
            x = list(range(1, months + 1))
            y = []
            remaining_balance = principal

            for month in range(1, months + 1):
                interest_payment = remaining_balance * monthly_interest_rate
                principal_payment = monthly_payment - interest_payment
                remaining_balance -= principal_payment
                y.append(remaining_balance)

            # Вывод графика
            plt.plot(x, y)
            plt.xlabel('Месяц')
            plt.ylabel('Остаток долга')
            plt.title('График погашения кредита')
            plt.grid(True)
            plt.show()

        window = Toplevel()
        window.title("Калькулятор расчета сложного процента")
        window.geometry('300x250')
        window.iconbitmap(r'Mkb.ico')

        # Метка с выбором типа расчета
        calculation_type_label = Label(window, text="Выберите тип расчета:")
        calculation_type_label.pack()

        # Выбор типа расчета (кредит или депозит)
        calculation_type = StringVar(window)
        calculation_type.set('Выберите тип расчета')  # Значение по умолчанию
        calculation_type_dropdown = OptionMenu(
            window, calculation_type, "Рассчитать кредит", "Рассчитать депозит", 'Выберите тип расчета')
        calculation_type_dropdown.pack()

        # Метки и поля ввода данных
        principal_label = Label(window, text="Сумма:")
        principal_label.pack()
        principal_entry = Entry(window)
        principal_entry.pack()

        interest_rate_label = Label(window, text="Процентная ставка:")
        interest_rate_label.pack()
        interest_rate_entry = Entry(window)
        interest_rate_entry.pack()

        time_period_label = Label(window, text="Срок (в годах):")
        time_period_label.pack()
        time_period_entry = Entry(window)
        time_period_entry.pack()

        # Кнопка для расчета
        calculate_button = Button(
            window, text="Рассчитать", command=on_calculation_type_selected, bg='#D9042B', font='Arial 10 bold', width=10,
            foreground='white')
        calculate_button.pack()

        # Кнопка для графиков
        graph_button = Button(
            window, text="Построить \n график", command=generate_payment_schedule, bg='#D9042B', font='Arial 10 bold', width=10,
            foreground='white')
        graph_button.pack()

    def inst():  # Скрытая кнопка, открывающаяся, после регистрации
        inst = Toplevel()
        inst.title('Инструкция пользователя')
        inst.iconbitmap(r'Mkb.ico')

        Label(inst, text=f'Вам доступны следующие опции:').grid(
            row=1, columnspan=3)

        Button(inst, text='Взять \n кредит', command=instrac.credit, bg='#D9042B', font='Arial 10 bold', width=10,
               foreground='white').grid(
            row=2, column=0)
        Button(inst, text='Сделать \n депозит', command=instrac.depos, bg='#D9042B', font='Arial 10 bold', width=10,
               foreground='white').grid(
            row=2, column=1)
        Button(inst, text='Рассчитать \n стоимость', command=instrac.rasch, bg='#D9042B', font='Arial 10 bold', width=10,
               foreground='white').grid(
            row=2, column=2)


def url1():
    url = 'https://mkb.ru/personal/deposits'
    requests.get(url)


def url2():
    url = 'https://mkb.ru/personal/credits'
    requests.get(url)
# Функция регистрации для новых пользователей


def reg():
    reg = Toplevel()
    reg.title('Регистрация')
    reg.iconbitmap(r'Mkb.ico')

    Label(reg, text='Авторизация в приложении', bg='#D9042B', font='Arial 10 bold',
          foreground='white').grid(row=1, column=1)
    Label(reg, text='Логин', bg='#272C8C', font='Arial 10 bold', width=10,
          foreground='white').grid(row=2, column=0)
    Label(reg, text='Пароль', bg='#272C8C', font='Arial 10 bold', width=10,
          foreground='white').grid(row=3, column=0)

    enewl = Entry(reg, width=80)
    enewl.grid(row=2, column=1)
    enewp = Entry(reg, width=80)
    enewp.grid(row=3, column=1)

    Button(reg, command=lambda: new(enewl, enewp), text='Зарегистрироваться', bg='#D9042B', font='Arial 10 bold', width=18,
           foreground='white').grid(row=4, column=1)


def new(enewl, enewp):  # Функция записи новых пользователей
    login = enewl.get()
    password = enewp.get()
    try:
        i = 0
        while i != 5:
            1/(len(login)-i)
            1/(len(password)-i)
            i += 1
    except:
        messagebox.showerror(
            'Ошибка', "Логин и пароль должны иметь длину больше 5 символов!")
    if len(login) > 5:
        if len(password) > 5:
            messagebox.showinfo(
                'Успешно!', f"Регистрация прошла успешно \n Ваш логин {login} \n Ваш пароль {password} ")
            with open('users.txt', 'a', encoding='utf-8') as file:
                file.write(login + '\n')
                file.write(password + '\n')


def old(eoldl, eoldp):  # Функция проверки входа
    login = eoldl.get()
    password = eoldp.get()
    with open('users.txt', 'r', encoding='utf-8') as file:
        for i in file:
            if i.strip() == login:
                log = True
            if i.strip() == password:
                pas = True
        if (log and pas) == True:
            Label(text="Вы вошли в систему!").grid(row=8, column=1)
    instr.config(state='active')

# Меню, выскакивающее для ответов на часто задаваемые вопросы


def vopr():
    vopr = Toplevel()
    vopr.title('часто задаваемые вопросы')
    vopr.iconbitmap(r'Mkb.ico')

    Label(vopr, foreground='white', bg='#D9042B',
          text='Как получить кредит в Мкб?').grid(row=0, column=0)
    Label(vopr, text='').grid(row=1, column=0)
    Label(vopr, foreground='white', bg='#272C8C', text='Чтобы взять кредит в Московском кредитном банке,\n можно обратиться в отделение банка или подать заявку через интернет. \nВ первом случае необходимо заполнить анкету и отдать ее сотрудникам банка вместе с документами.').grid(row=3, column=1)

    Label(vopr, text='').grid(row=3, column=0)
    Label(vopr, foreground='white', bg='#D9042B',
          text='На каком месте МКБ?').grid(row=4, column=0)
    Label(vopr, text='').grid(row=5, column=0)
    Label(vopr, foreground='white', bg='#272C8C', text='Московский Кредитный Банк занимает 7 место\n по размеру активов среди банков России. \nПоказать весь рейтинг банков по размеру активов. \nВ январе 2022 Московский Кредитный Банк располагался на 7 месте,\n таким образом, за месяц позиция в рейтинге не изменилась.').grid(row=6, column=1)

    Label(vopr, text='').grid(row=7, column=0)
    Label(vopr, foreground='white', bg='#D9042B',
          text='Сколько клиентов у МКБ?').grid(row=8, column=0)
    Label(vopr, text='').grid(row=9, column=0)
    Label(vopr, foreground='white', bg='#272C8C',  text='Активы МКБ,\n согласно российским стандартам бухгалтерского учета,\n по состоянию на 1 сентября 2021 года составляют 3,1 трлн рублей. \nЧисло розничных клиентов банка превышает 1,7 млн человек, \nа корпоративных клиентов — более 15 тыс').grid(row=10, column=1)


Label(image=test).grid(row=0, column=0)
logo = Label(text='МКБ', foreground='Red',
             font='Arial 16 bold').grid(row=0, column=1)

# Меню
Button(text='Вход в систему', width=15, height=5, font='Arial 11',
       bg='#D90D43', foreground='#F2F2F2').grid(row=1, column=0)
instr = Button(text='Инструкция\n пользователя', command=instrac.inst, width=15, height=5, state='disabled', font='Arial 11',
               bg='#D90D43', foreground='#F2F2F2')
instr.grid(row=1, column=1)
Button(text='Регистрация', command=reg, width=15, height=5, font='Arial 11',
       bg='#D90D43', foreground='#F2F2F2').grid(row=1, column=2)
Button(text='Часто задаваемые\n вопросы', command=vopr, width=15, height=5, font='Arial 11',
       bg='#D90D43', foreground='#F2F2F2').grid(row=1, column=3)

# Отступы
Label().grid(row=2)
Label().grid(row=6)
Label().grid(row=8)
Label().grid(row=10)
Label().grid(row=13)

# Отображение Входа
Label(text='Логин', bg='#272C8C', font='Arial 10 bold', width=10,
      foreground='white').grid(row=3, column=0)
Label(text='Пароль', bg='#272C8C', font='Arial 10 bold', width=10,
      foreground='white').grid(row=5, column=0)
eoldl = Entry(width=80)
eoldl.grid(row=3, column=1, columnspan=3)
eoldp = Entry(width=80, show='*')
eoldp.grid(row=5, column=1, columnspan=3)
Button(text='Войти', command=lambda: old(eoldl, eoldp), bg='#D9042B', font='Arial 10 bold', width=10,
       foreground='white').grid(row=7, column=1)

Label(text="Для получения большего функционала\nзарегистрируйтесь или войдите").grid(
    row=7, column=5)

# Общая информация
Label(
    font='Arial 7',
    text='Публичное акционерное общество\n «Московский кредитный банк» — крупнейший негосударственный публичный банк в России,\n осуществляющий коммерческую деятельность в 22 регионах\n Центрального, Приволжского, Северо-Западного и Уральского федеральных округов.\n Включён Банком России в перечень системно значимых кредитных организаций. Головной офис расположен в Москве.'
).grid(columnspan=4)

root.mainloop()
