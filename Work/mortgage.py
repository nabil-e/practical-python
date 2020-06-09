# mortgage.py
#
# Exercise 1.7: Dave’s mortgage

pret = 500000
interet = 0.05
mensualite = 2684.11
payement_total = 0

while pret > 0:
    pret = pret * (1+interet/12) - mensualite
    payement_total += mensualite

print(round(payement_total, 1))