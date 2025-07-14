#!/usr/bin/env python3

'''
Script for take a markdown file with final questions and make it ready for anki card conversion.
Save it to new markdown file with _ankiready appended to the filename.
Author: Felicia Fredlund
Last updated: 2025-07-XX

How to run:
python(3) FILENAME.py PATH/FILE.md
'''

'''
THIS IS WHAT THE OUTPUT SHOULD LOOK LIKE:

"<b>Hierarchical Network Model.</b> Kursmaterialet listar 6 fördelar som kan uppnås med den hierarkiska nätverksmodellen. (6p)<br><br>
<b>a.</b> Vilka är dessa fördelar?<br>
<b>b.</b> Ge exempel på hur man får eller på vilket sätt man erhåller dessa fördelar.<br>
<img src=""hierarchical-network-model.png"">";


THIS IS AN UNEDITED QUESTION:
    OBS!!!
    1. NOT ALL FINALS USE COLON, IT COULD USE PERIOD.
    SO CHECK IF THERE IS A COLON, IF NOT USE THE FIRST PERIOD)
    2. THERE CAN BE QUITE MANY a./b./c. SO TRY AND FIND AN EASY WAY TO CHECK FOR THAT.

1. Filsystemslayout: Alla bibliotek i en Linux har sitt bestämda ändamål. Beskriv ändamålet för följande bibliotek. (4p)
a. /bin
b. /mnt
c. /home
d. /etc
'''

test = """
1. Filsystemslayout: Alla bibliotek i en Linux har sitt bestämda ändamål. Beskriv ändamålet för följande bibliotek. (4p)
a. /bin
b. /mnt
c. /home
d. /etc

1. Filsystemslayout. Alla bibliotek i en Linux har sitt bestämda ändamål. Beskriv ändamålet för följande bibliotek. (4p)
a. /bin
b. /mnt
c. /home
d. /etc
"""

lines = test.splitlines()
previous_index = -1

for i in range(len(lines)):
    line = lines[i].strip()
    if line == "":
        if previous_index != -1:
            lines[previous_index] += '";'
        continue
    
    if line[0].isdigit():
        line = line[3:]
        
        bold_index = line.find(":")
        if bold_index == -1:
            bold_index = line.find(".")
        
        line = line[:bold_index + 1] + "</b>" + line[bold_index + 1:]

        line = '"<b>' + line + '<br><br>'
    elif line[0].isalpha():
        line = "<b>" + line[:2] + "</b>" + line[2:] + "<br>"
    else:
        line = "ERROR " + line + " ERROR"
    
    lines[i] = line
    
    previous_index = i
