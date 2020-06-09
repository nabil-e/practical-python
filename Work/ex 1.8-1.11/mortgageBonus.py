# mortgageBonus.py
#
# Exercise 1.11: Bonus
pret = 500000
interet = 0.05
mensualite = 2684.11

extra_payment_start_month = 60 # int(input('Wath\'s your extra payment start month: '))
extra_payment_end_month = 108 # int(input('Wath\'s your extra payment end month: '))
extra_payment = 1000 # int(input('Wath\'s your extra payment: '))

total_paid = 0
month = 0

while pret > 0:
    if pret < mensualite:
        mensualite = pret
        pret -= mensualite
        total_paid += mensualite
        month += 1
        print(f'{month} {round(total_paid, 2)} {round(pret, 2)} ')
    else:
        pret = pret * (1+interet/12) - mensualite
        total_paid += mensualite
        month += 1
        print(f'{month} {round(total_paid, 2)} {round(pret, 2)} ')
        if month >= extra_payment_start_month and month <= extra_payment_end_month:
            pret -= extra_payment
            total_paid += extra_payment
        
print(f'Payement total: {round(total_paid, 2)} en {month} mois.')