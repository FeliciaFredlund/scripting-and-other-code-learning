'''
Script for changing a Swedish text to rövarspråket
Author: Felicia Fredlund
Last updated: 2025-02-10

How to run:
python(3) rovarspraket.py

Examples:
python3 rovarspraket.py
python rovarspraket.py
'''

def rovarspraket(text):
    vowels = "aeiouyåäö"
    translated_text = ""
    for char in text:
        if char not in vowels and char.isalpha():
            translated_text += char + "o" + char.lower()
        else:
            translated_text += char

    return translated_text

def main():
    phrase = input("Skriva vad du vill översätta till rövarspråket: ")
    print("Översatt:", rovarspraket(phrase))

main()
