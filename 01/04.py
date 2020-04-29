def bank(amount, duration, percent):
    return amount * (1 + percent / 100) ** duration


try:
    amount = float(input('Какая сумма депозита?'))
    duration = float(input('Какая срок депозита (лет)?'))
    percent = float(input('Какая процентная ставка депозита?'))

    print(f'\nПо истечении депозита сумма составит {bank(amount, duration, percent):.2f}')

except ValueError:
    print('Подходят только числовые значения')



