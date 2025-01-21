'''
Script for the amount of ingredients needed for sockerkaka for different amounts of people
Author: Felicia Fredlund
Last updated: 2025-01-21

How to run:
python(3) lab1-recept.py NUMBER_OF_PEOPLE

Examples:
python3 lab1-recept.py 1
python lab1-recept.py 15
'''
import sys


def sockerkaka(antal):  
    print(f"\n*** Sockerkaka för {antal} ***\n")

    antal = float(antal)

    print("Till formen:")
    print(f"ca {(15/4 * antal):g} g smör")
    print(f"ca {(3/4 * antal):g} msk ströbröd\n")

    print("Till sockerkakan:")
    print(f"ca {(3/4 * antal):g} st ägg")
    print(f"ca {(3/4 * antal):g} dl strösocker")
    print(f"ca {(0.5 * antal):g} tsk vaniljsocker")
    print(f"ca {(0.5 * antal):g} tsk bakpulver")
    print(f"ca {(3/4 * antal):g} dl mjöl")
    print(f"ca {(75/4 * antal):g} g smör")
    print(f"ca {(0.25 * antal):g} dl vatten\n")

    print("Instruktionerna för receptet finns här: http://www.recepten.se/recept/sockerkaka.html")

def main():
    if (len(sys.argv) < 2):
        print("ERROR: Ingen parameter angiven. (Antalet personer)")
        return

    number_of_people = int(sys.argv[1])
    
    sockerkaka(number_of_people)

main()