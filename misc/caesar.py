#!/usr/bin/env python3
from sys import exit

letters = []
for l in range(ord("a"), ord("z")+1):
    letters.append(chr(l))
letters_mod = len(letters)

def msg_inp():
    global task, msg, shf
    task = input("To encode \tenter 1,\nto decode \tenter 2,\nto exit \tenter 0: ")
    if task != "1" and task != "2":
        print("Exiting...")
        exit()
    msg = input("Your message: ").lower()
    shf = int(input("Shift value: "))
    return(task, msg, shf)

def caesar(m, s):
    caesar = ""
    if task == "2":
        s *= -1
    for i in m:
        if i in letters:
            caesar += letters[(letters.index(i) + s) % letters_mod]
        else:
            caesar += i
    return(caesar)

task = "1"
while task == "1" or task == "2":
    msg_inp()
    code = caesar(m = msg, s = shf).upper()
    if task == "1":
        print(f"Encoded: {code}")
    elif task == "2":
        code = caesar(m = msg, s = shf).upper()
        print(f"Decoded: {code}")
        print("Other possible solutions:")
        for n in range(len(letters)):
            print("+", shf, caesar(m = msg, s = n).upper())
    else:
        print("How?")
    print("\n") 