#!/bin/python3

letters = {
    "A": "Б",
    "B": "Ш",
    "C": "Г",
    "D": "D",
    "E": "∈",
    "F": "ƒ",
    "G": "G",
    "H": "h",
    "I": "ſ",
    "J": "J",
    "K": "K",
    "L": "⌡",
    "Y": "y",
    "M": "m",
    "N": "n",
    "O": "c",
    "P": "P",
    "Q": "Ф",
    "R": "Я",
    "S": "∫",
    "T": "T",
    "U": "U",
    "V": "V",
    "W": "W",
    "X": "X",
    "Z": "z",
    " ": " "
}

while True:
    try: sentence = input("")
    except: break

    formatted = ""

    for char in sentence:
        if char.upper() in letters:
            formatted += letters[char.upper()]
        else:
            formatted += char

    print(formatted)
