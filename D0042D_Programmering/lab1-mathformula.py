'''
Skript för att räkna ut total kostnaden för ett lån med rak amortering
Author: Felicia Fredlund
Last updated: 2025-01-21

How to run:
python(3) lab1-mathformula.py LÅNE_BELOPP ÅRLIG_RÄNTA ANTAL_ÅR

Examples:
python3 lab1-mathformula.py 50000 0.03 10
python lab1-mathformula.py 10000 0.1 5
'''
import sys

# p = lånade beloppet
# r = årliga räntesatsen
# a = antal år för återbetalning
def kostnad(p, r, a):  
    formula = p + (a + 1) * p * r/2
    print("Kostnaden för ett lån\n")
    print(f"Lån belopp: {p}")
    print(f"Räntesats: {r}")
    print(f"Antal år: {a}\n")
    print(f"Kostnad: {formula:g}")

def main():
    if (len(sys.argv) < 4):
        print("ERROR: Inte tillräcklig många parametrar angivna.")
        return

    p = int(sys.argv[1])
    r = float(sys.argv[2])
    a = int(sys.argv[3])
    
    kostnad(p, r, a)

main()