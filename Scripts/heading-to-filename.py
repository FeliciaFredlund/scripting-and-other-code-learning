# Start to a reusable script to take headings or other text and change it to a filename that works cross-platform

import string

def character_replace(c):
    if c in string.punctuation or c == " ":
        return "-"
    return c

name = "HEADING"
print("".join(map(character_replace, name)).replace("--", "-").replace("--", "-").replace("--", "-").strip("-"))