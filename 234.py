import matplotlib.pyplot as plt


def generate_payment_schedule(principal, interest_rate, years):
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


# Пример использования
principal = 10000
interest_rate = 10
years = 3

generate_payment_schedule(principal, interest_rate, years)
