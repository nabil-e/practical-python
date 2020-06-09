# extrapayments.py
#
# Exercise 1.8: Extra payments

pret = 500000
interet = 0.05
mensualite = 2684.11
extra = 1000
payement_total = 0
month = 0
for i in range(12):
    pret = pret * (1+interet/12) - mensualite - extra
    payement_total += mensualite + extra
    month += 1
while pret > 0:
    
    pret = pret * (1+interet/12) - mensualite
    payement_total += mensualite
    month += 1
print(f'Payement total: {round(payement_total, 2)} en {month} mois.')
